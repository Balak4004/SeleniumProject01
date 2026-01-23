

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class FreeTrialPage:

    def __init__(self,driver):
        self.driver = driver

    username_email_ft = (By.XPATH,"//input[@id='page-v1-step1-email']")
    checkbox_terms = (By.XPATH,"//input[@id='page-free-trial-step1-cu-gdpr-consent-checkbox']")
    button_click_ft = (By.XPATH, "//button[normalize-space()='Create a Free Trial Account']")
    error_msg_invalid_email = (By.XPATH,"//div[normalize-space()='The email address you entered is incorrect.']")

    def get_username_ft(self,timeout=7):
        wait=WebDriverWait(self.driver,timeout)
        return wait.until(EC.visibility_of_element_located(FreeTrialPage.username_email_ft))

    def get_checkbox_terms(self,timeout=7):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(FreeTrialPage.checkbox_terms))

    def get_button_click_ft(self,timeout=7):
        wait=WebDriverWait(self.driver,timeout)
        return wait.until(EC.visibility_of_element_located(FreeTrialPage.button_click_ft))

    def get_error_msg(self,timeout=7):
        wait=WebDriverWait(self.driver,timeout)
        return wait.until(EC.visibility_of_element_located(FreeTrialPage.error_msg_invalid_email))

    def get_error_msg_text(self,timeout=7):
        wait=WebDriverWait(self.driver,timeout)
        error_msg_element = wait.until(EC.visibility_of_element_located(self.error_msg_invalid_email))
        return error_msg_element.text

    def enter_free_trail_details_invalid(self,invalid_email,timeout=5):
       try:
           self.get_username_ft().send_keys(invalid_email)
           self.get_checkbox_terms().click()
           wait = WebDriverWait(self.driver, timeout)
           wait.until(EC.visibility_of_element_located(self.button_click_ft))
           self.get_button_click_ft().click()
       except Exception as e:
           print(e)


