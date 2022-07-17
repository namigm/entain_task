from locators.Locators_main import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen


class Watchlist:
    logger = LogGen.loggen()

    def __init__(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 20)
        self.targetFilmTitle = ''

    def target_film_title(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, Locators.targetFilmTitle_class)))
        targetFilmTitle = \
            self.driver.find_elements(By.CLASS_NAME, Locators.targetFilmTitle_class)[2].text.split("\n")[
                1]
        return targetFilmTitle

    def wl_btn_main(self):
        self.driver.find_element(By.XPATH, Locators.wlBtnMainPage_xpath).click()

    def wl_titles_count(self):
        titlesCount = int(self.driver.find_element(By.XPATH, "//div[@class='lister-details']").text.split(' ')[0])
        return int(titlesCount)

    def wl_check_1film(self):
        wlFilm = self.driver.find_element(By.XPATH, Locators.wlCheckFilm_xpath).text
        return wlFilm

    def wl_clean(self):
        self.driver.find_element(By.XPATH, Locators.wlEdit_xpath).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.wlLabel_xpath)))
        self.driver.find_element(By.XPATH, Locators.wlLabel_xpath).click()
        self.driver.find_element(By.CSS_SELECTOR, Locators.wlDeleteBtn_css).click()
        self.wait.until((EC.element_to_be_clickable((By.XPATH, Locators.wlContentSubDel_xpath))))
        self.driver.find_element(By.XPATH, Locators.wlContentSubDel_xpath).click()

    def add_film_to_wl(self):
        self.targetFilmTitle = self.target_film_title()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, Locators.targetFilmGroup_class)))
        target_film = self.driver.find_elements(By.CLASS_NAME,
                                                Locators.targetFilmGroup_class)[2]. \
            find_element(By.CLASS_NAME, Locators.targetFilm_class)
        target_film.click()

    def check_film_in_wl(self):
        actual_title = self.driver.title
        if actual_title == 'Your Watchlist - IMDb':
            if self.wl_titles_count() == 1:
                if self.targetFilmTitle in self.wl_check_1film():
                    self.logger.info("*************** Test001WatchlistAdd/test_watchlist_add is passed ***************")
                    self.wl_clean()
                    assert True
                else:
                    self.logger.info(f"*Test001WatchlistAdd/test_watchlist_add - failed/wrong film title/"
                                     f"film title captured as{self.targetFilmTitle} *")
                    self.wl_clean()
                    assert False
            elif self.wl_titles_count() == 0:
                self.logger.info("****** Test001WatchlistAdd/test_watchlist_add is failed/film not added to wl ******")
                assert False
        else:
            self.driver.get_screenshot_as_file(r"entain_task/screenshots/test_watchlist_add.png")
            self.logger.info("******* Test001WatchlistAdd/test_watchlist_add - watchlist page issue *******")
            assert False
