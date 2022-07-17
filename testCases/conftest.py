import pytest
from selenium import webdriver
from utilities.readproperties import ReadConfig
from pageObjects.LoginPage import Login


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def base_fixture(setup):
    driver = setup
    driver.get(ReadConfig.get_url())
    lp = Login(driver)
    lp.signin_btn()
    lp.login_imdb()
    yield
    lp.logout()
    driver.close()


def pytest_addoption(parser):  # value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # return the Browser to setup method
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project name'] = 'entain task'
    config._metadata['Tester'] = 'NamigM'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
