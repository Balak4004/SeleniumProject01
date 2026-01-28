
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.test.utils.Utils import take_screenshot
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):

    def __init__(self,driver):
        self.driver = driver
        self.highlight = True

    locators = {
    'username' : ('ID', "login-username"),
    'password' : ('ID', "login-password"),
    'submit_button' : ('ID', "js-login-btn"),
    'error_msg' : ('CLASS_NAME', "notification-box-description")
    }


    def login_to_vwo(self,usr,pwd):
       self.username.set_text(usr)
       self.password.set_text(pwd)
       self.submit_button.click_button()

    def get_error_msg(self, timeout=10):
       return self.error_msg.text
'''
    def get_error_msg(self, timeout=10):
        locator = (By.CLASS_NAME, "notification-box-description")
        error_element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return error_element.text
        '''




