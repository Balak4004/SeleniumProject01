
import time

import pytest

import allure
from selenium import webdriver
from src.test.constants.Constants import Constants
from dotenv import load_dotenv
import os

from src.test.pageObjects.Cura.MakeAppointment import MakeAppointment
from src.test.utils.Utils import take_screenshot

@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants().app_cura_url())
    return driver


def test_make_appointmnet(setup):
    driver = setup
    make_appointment_page = MakeAppointment(driver)
    make_appointment_page.make_appointment()
    time.sleep(5)
    take_screenshot(driver=driver, name="make appointment button click")

    assert make_appointment_page.get_current_url() == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    make_appointment_page.login("John Doe","ThisIsNotAPassword")
    time.sleep(5)
    take_screenshot(driver=driver, name="login button click")


    time.sleep(3)
    driver.quit()




