import pytest
import requests
import allure
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="run tests in headless mode")
    parser.addoption("--browsers", action="store", default="chrome,firefox",
                     help="comma-separated list of browsers to test: chrome,firefox")


def pytest_generate_tests(metafunc):
    if "driver" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("--browsers").split(",")
        metafunc.parametrize("driver", browsers, indirect=True)


@pytest.fixture()
def driver(request):
    browser_name = request.param
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        if headless:
            chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")

        if headless:
            firefox_options.add_argument("--headless")

        driver = webdriver.Firefox(options=firefox_options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)

    from urls import Urls
    driver.get(Urls.BASE_URL)

    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    from data import TestData
    from locators.main_page_locators import MainPageLocators

    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.click_login_button()
    login_page.login(TestData.TEST_EMAIL, TestData.TEST_PASSWORD)

    main_page.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY)

    return driver


@pytest.fixture()
def revert_avatar():
    from data import TestData
    from urls import Urls

    credentials = {
        "email": TestData.TEST_EMAIL,
        "password": TestData.TEST_PASSWORD,
    }

    response = requests.post(Urls.AUTH_ENDPOINT, json=credentials)
    token = response.json().get("token")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    update_data = {
        "avatar": Urls.DEFAULT_AVATAR_URL,
    }
    requests.patch(Urls.AVATAR_UPDATE_ENDPOINT, json=update_data, headers=headers)

    yield