
import time
import pytest
import allure

from selenium import webdriver
from src.test.constants.Constants import Constants
from dotenv import load_dotenv
import os

from src.test.pageObjects.idrive.loginpage import IDriveLoginPage
from src.test.pageObjects.idrive.idriveDashBoardPage import IDriveDashboardPage

from src.test.utils.Utils import take_screenshot



@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants().app_i_drive_url())
    time.sleep(10)
    return driver

@allure.title("idrive dashboard test case")
@allure.description("TC#1 idrive dashboard test case - update the plan")
@pytest.mark.negativevwologin
def test_login_to_i_drive_valid_details(setup):
    driver = setup
    login_page = IDriveLoginPage(driver)
    login_page.login_to_idrive(usr=os.getenv("idrive_username"),
                               pwd=os.getenv("idrive_password"))
    time.sleep(15)
    take_screenshot(driver=driver, name="Positive test case")

    assert login_page.get_current_url() == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    dashboard_page = IDriveDashboardPage(driver)
    assert dashboard_page.get_ft_expired_msg_text() == "Your free trial has expired!"
    assert dashboard_page.get_upd_msg_btn_text() == "Upgrade Now!"

    dashboard_page.update_plan_details()
    take_screenshot(driver=driver, name="renewal page screenshot")

    assert dashboard_page.get_current_url_end() == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    time.sleep(2)
    driver.quit()


