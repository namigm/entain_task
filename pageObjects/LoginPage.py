from locators.Locators_main import Locators
from selenium.webdriver.common.by import By
from utilities.readproperties import ReadConfig


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login_imdb_btn(self):
        logImdbBtn = self.driver.find_element(By.XPATH, Locators.logImdbBtn_xpath)
        logImdbBtn.click()

    def _set_imdb_email(self):
        logImdbEmail = self.driver.find_element(By.XPATH, Locators.logEmail_xpath)
        logImdbEmail.send_keys(ReadConfig.imdb_login())

    def _set_imdb_pass(self):
        logImdbPass = self.driver.find_element(By.XPATH, Locators.logPass_xpath)
        logImdbPass.send_keys(ReadConfig.imdb_password())

    def imdb_submit_btn(self):
        logSubmitBtn = self.driver.find_element(By.XPATH, Locators.signInSubmit_xpath)
        logSubmitBtn.click()

    def signin_btn(self):
        signInBtn = self.driver.find_element(By.XPATH, Locators.signInnBtn_xpath)
        signInBtn.click()

    def logout(self):
        self.driver.refresh()
        self.driver.find_element(By.XPATH, Locators.toggleAccountMenu_xpath).click()
        self.driver.find_element(By.XPATH, Locators.signOut_xpath).click()

    def login_imdb(self):
        self.login_imdb_btn()
        self._set_imdb_email()
        self._set_imdb_pass()
        self.imdb_submit_btn()


