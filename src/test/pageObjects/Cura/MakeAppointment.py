

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.test.utils.Utils import take_screenshot

class MakeAppointment:

    def __init__(self, driver):
        self.driver = driver

    #Page Locators
    appointment_button = (By.ID,"btn-make-appointment")
    username1 = (By.ID, "txt-username")
    password1 = (By.ID, "txt-password")
    login_btn = (By.ID, "btn-login")


    # Page Actions
    def get_appointment_button(self):
        return self.driver.find_element(*self.appointment_button)

    def get_username1(self):
        return self.driver.find_element(*self.username1)

    def get_password1(self):
        return self.driver.find_element(*self.password1)

    def get_login_btn(self):
        return self.driver.find_element(*self.login_btn)

    def make_appointment(self,timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            take_screenshot(driver=self.driver, name="make appointment page")
            wait.until(EC.element_to_be_clickable(self.appointment_button)).click()

        except Exception as e:
            raise e

    def get_current_url(self):
        return self.driver.current_url

    def login(self,username1,password1,timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(self.username1)).send_keys(username1)
            wait.until(EC.visibility_of_element_located(self.password1)).send_keys(password1)
            take_screenshot(driver=self.driver, name="login page")
            wait.until(EC.element_to_be_clickable(self.login_btn)).click()
        except Exception as e:
            raise e





