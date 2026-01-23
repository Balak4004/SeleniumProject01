import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IDriveLoginPage:

    def __init__(self,driver):
        self.driver = driver

    user_name_ip = (By.XPATH,"//input[@id='username']")
    password_ip = (By.XPATH,"//input[@id='password']")
    remember_check_box = (By.XPATH,"//span[@tabindex='-1']")
    sign_in_btn = (By.XPATH,"//button[normalize-space()='Sign in']")

    #def get_user_name_ip(self):
        #webdriver_wait(driver=self.driver, element_tuple=self.user_name_ip, timeout=10)
        #return self.driver.find_element(*IDriveLoginPage.user_name_ip)

    def get_user_name_ip(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.user_name_ip)
        )

    def get_password_ip(self):
        return self.driver.find_element(*IDriveLoginPage.password_ip)

    def get_remember_check_box(self):
        return self.driver.find_element(*IDriveLoginPage.remember_check_box)

    def get_sign_in_btn(self):
        return self.driver.find_element(*IDriveLoginPage.sign_in_btn)

    def login_to_idrive(self,usr,pwd):
        try:
            self.get_user_name_ip().send_keys(usr)
            self.get_password_ip().send_keys(pwd)
            self.get_remember_check_box().click()
            self.get_sign_in_btn().click()
            time.sleep(20)
        except Exception as e:
            print(e)

    def get_current_url(self):
        print(self.driver.current_url)
        return self.driver.current_url
