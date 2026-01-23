import time
import allure
import pytest
# Webdriver start
# User Interaction + Assertion
# Close driver

from selenium import webdriver
from src.test.constants.Constants import Constants
from dotenv import load_dotenv
import os

from src.test.pageObjects.vwo.Loginpage import LoginPage
from src.test.pageObjects.vwo.freeTrialPage import FreeTrialPage

from src.test.utils.Utils import take_screenshot


@pytest.fixture
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants().app_url())
    return driver


@allure.title("Vwo free trail test case")
@allure.description("TC#1 Free trial test case - Login with invalid email")
@pytest.mark.negativevwologin
def test_free_trial_Negative(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.ft_button_click()
    take_screenshot(driver=driver, name="test_vwo_ft_negative")
    free_trial_page = FreeTrialPage(driver)
    free_trial_page.enter_free_trail_details_invalid("admin")
    error_msg_invalid_email_text = free_trial_page.get_error_msg_text()
    take_screenshot(driver=driver,name="test_vwo_login_negative")

    assert error_msg_invalid_email_text == "The email address you entered is incorrect."
