
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):

        self.driver = driver

    #Page Locators
    Email_address_element = (By.ID, "login-username")
    Password_element = (By.ID, "login-password")
    sign_in_button = (By.ID, "js-login-btn")
    error_msg = (By.CLASS_NAME, "notification-box-description")

    # Page Actions
    def get_Email_address_element(self):
        return self.driver.find_element(*LoginPage.Email_address_element)

    def get_Password_element(self):
        return  self.driver.find_element(*LoginPage.Password_element)

    def get_sign_in_button(self):
        return self.driver.find_element(*LoginPage.sign_in_button)

    def login_to_vwo(self,usr,pwd):
        try:
            self.get_Email_address_element().send_keys(usr)
            self.get_Password_element().send_keys(pwd)
            self.get_sign_in_button().click()
        except Exception as e:
            print(e)



