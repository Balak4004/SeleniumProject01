
import time
import pytest

import allure
from selenium import webdriver
from src.test.constants.Constants import Constants
from dotenv import load_dotenv
import os

from src.test.pageObjects.Cura.MakeAppointment import MakeAppointment
from src.test.pageObjects.Cura.CuraDashboard import AppointmentDashboard
from src.test.utils.Utils import take_screenshot

'''
@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants().app_cura_url())
    return driver
'''

@pytest.fixture()
def setup():
    # to prevent update password chrome pop up
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(Constants().app_cura_url())
    return driver


def test_make_appointmnet(setup):
    driver = setup
    make_appointment_page = MakeAppointment(driver)
    make_appointment_page.make_appointment()
    time.sleep(3)
    assert make_appointment_page.get_current_url() == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    make_appointment_page.login("John Doe","ThisIsNotAPassword")
    time.sleep(1)
    take_screenshot(driver=driver, name="login button click")
    time.sleep(1)

    appointment_page = AppointmentDashboard(driver)
    time.sleep(5)
    appointment_page.appointment_page(
        facility_name="Hongkong CURA Healthcare Center",
        visitdate = "17/11/2025",
        comment = "test comment")
    time.sleep(2)

    assert appointment_page.get_new_url() == "https://katalon-demo-cura.herokuapp.com/appointment.php#summary"
    assert appointment_page.get_confirm_msg_text() == "Appointment Confirmation"

    time.sleep(3)
    driver.quit()




