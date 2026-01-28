import time
import pytest

import allure
from selenium import webdriver
from src.test.constants.Constants import Constants
from src.test.pageObjects.vwo.Loginpage_PF import LoginPage
from dotenv import load_dotenv
import os

from src.test.pageObjects.vwo.dashboardPage_PF import DashboardPage
from src.test.utils.Utils import take_screenshot

@allure.epic("VWO Login")
@allure.feature("Login")
class TestVwoLogin:

    @pytest.mark.qa
    def test_vwo_login_positive(self, setup):
        try:
            driver = setup
            driver.get(Constants().app_url())
            username = os.getenv("VALID_USERNAME")
            password = os.getenv("VALID_PASSWORD")
            login_page = LoginPage(driver)
            login_page.login_to_vwo(usr=username, pwd=password)
            dashboard_page = DashboardPage(driver)
            username = dashboard_page.user_logged_in_text()
            take_screenshot(driver=driver, name="vwo login postibe with pagefactory")
            assert username == os.getenv("USERNAME_LOGGED_IN")

        except Exception as e:
            raise e

    @pytest.mark.qa
    def test_vwo_login_negative(self,setup):
        try:
            driver = setup
            driver.get(Constants().app_url())
            username = os.getenv("INVALID_USERNAME")
            password = os.getenv("INVALID_PASSWORD")
            login_page = LoginPage(driver)
            login_page.login_to_vwo(usr=username,pwd=password)
            error_msg_text = login_page.get_error_msg()
            print(error_msg_text)
            take_screenshot(driver=driver, name="vwo login negative with pagefactory")
            assert error_msg_text == os.getenv("error_message_expected")

        except Exception as e:
            raise e
