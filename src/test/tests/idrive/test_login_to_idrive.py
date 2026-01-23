
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
from src.test.utils.Utils import take_screenshot

from src.test.pageObjects.idrive.loginpage import IDriveLoginPage



@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants().app_i_drive_url())
    time.sleep(10)
    return driver

@allure.title("idrive login test case")
@allure.description("TC#1 idrive login test case - Login with valid creds")
@pytest.mark.negativevwologin
def test_login_to_i_drive_valid_details(setup):
    driver = setup
    login_page = IDriveLoginPage(driver)
    login_page.login_to_idrive(usr=os.getenv("idrive_username"),
                               pwd=os.getenv("idrive_password"))
    time.sleep(15)
    take_screenshot(driver=driver, name="Positive test case")

    assert login_page.get_current_url() == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    time.sleep(2)
    driver.quit()



