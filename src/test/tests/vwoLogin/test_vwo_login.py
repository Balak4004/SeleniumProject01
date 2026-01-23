import time

import pytest
# Webdriver start
# User Interaction + Assertion
# Close driver

import allure
from selenium import webdriver
from src.test.constants.Constants import Constants
from dotenv import load_dotenv
import os

from src.test.pageObjects.vwo.Loginpage import LoginPage
from src.test.pageObjects.vwo.dashboardPage import DashboardPage
from src.test.utils.Utils import take_screenshot


@pytest.fixture
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants().app_url())
    return driver


@allure.title("Vwo Login Negative test case")
@allure.description("TC#1 Negative test case - Login with invalid credentials")
@pytest.mark.negativevwologin
def test_vwo_login_negative(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login_to_vwo(usr=os.getenv("INVALID_USERNAME"),
                            pwd=os.getenv("INVALID_PASSWORD"))
    error_msg_element_text = login_page.get_error_message_as_text()
    take_screenshot(driver=driver,name="test_vwo_login_negative")

    assert error_msg_element_text == os.getenv("error_message_expected")

    time.sleep(3)
    driver.quit()


@allure.title("Vwo Login Positive test case")
@allure.description("TC#1 Positive test case - Login with valid credentials")
@pytest.mark.negativevwologin
def test_vwo_login_positive(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login_to_vwo(usr=os.getenv("VALID_USERNAME"),pwd=os.getenv("VALID_PASSWORD"))
    dashboard_page = DashboardPage(driver)
    user_name = dashboard_page.user_logged_in_text()
    take_screenshot(driver=driver,name="Positive test case")
    assert os.getenv("USERNAME_LOGGED_IN") == user_name
