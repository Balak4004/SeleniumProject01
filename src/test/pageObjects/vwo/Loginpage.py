
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.test.utils.Utils import take_screenshot

#from src.test.utils.common_utils import webdriver_wait


class LoginPage:

    def __init__(self,driver):

        self.driver = driver

    #Page Locators
    Email_address_element = (By.ID, "login-username")
    Password_element = (By.ID, "login-password")
    sign_in_button = (By.ID, "js-login-btn")
    error_msg = (By.CLASS_NAME, "notification-box-description")
    ft_button = (By.XPATH,"//a[normalize-space()='Start a free trial']")

    # Page Actions
    def get_Email_address_element(self):
        return self.driver.find_element(*LoginPage.Email_address_element)

    def get_Password_element(self):
        return  self.driver.find_element(*LoginPage.Password_element)

    def get_sign_in_button(self):
        return self.driver.find_element(*LoginPage.sign_in_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_msg)

    def login_to_vwo(self,usr,pwd):
        try:
            self.get_Email_address_element().send_keys(usr)
            self.get_Password_element().send_keys(pwd)
            self.get_sign_in_button().click()
        except Exception as e:
            print(e)

    def get_error_message_as_text(self, timeout=10):
        wait = WebDriverWait(self.driver,timeout)
        wait.until(EC.visibility_of_element_located(self.error_msg))
        return self.get_error_message().text

    def get_ft_button(self):
        return self.driver.find_element(*LoginPage.ft_button)

    def ft_button_click(self):
        try:
            self.get_ft_button().click()
        except Exception as e:
            print(e)



