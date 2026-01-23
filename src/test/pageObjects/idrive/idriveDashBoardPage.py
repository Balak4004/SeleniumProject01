import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.test.utils.Utils import take_screenshot

import traceback

class IDriveDashboardPage:

    def __init__(self,driver):
        self.driver = driver

    #Page Locators
    upd_msg_btn = (By.XPATH,"//button[normalize-space()='Upgrade Now!']")
    ft_expired_msg = (By.XPATH,"//h5[normalize-space()='Your free trial has expired!']")

    card_number = (By.XPATH,"//input[@name='cardnumber']")
    card_expiry = (By.XPATH,"//input[@name='exp-date']")
    card_cvv = (By.XPATH,"//input[@name='cvc']")
    bill_address = (By.XPATH,"//input[@id='upgradeaddress' and @name='billAddr']")
    country_dropdown = (By.XPATH,"//select[@name='countryname']/option[normalize-space()='India']")
    state_dropdown = (By.XPATH,"//select[@formcontrolname='state']/option[normalize-space()='Karnataka']")
    pin_code = (By.XPATH,"//input[@placeholder='Postal Code']")
    check_box = (By.XPATH,"//span[@tabindex='-1' and @class = 'id-checkmark']")
    upgrade_button = (By.XPATH,"//button[@id='frm-btn1']")


    # Page Actions
    def get_upd_msg_btn(self,timeout=5):
        wait = WebDriverWait(self.driver,timeout)
        return wait.until(EC.visibility_of_element_located(IDriveDashboardPage.upd_msg_btn))

    def get_upd_msg_btn_text(self,timeout=5):
        return self.get_upd_msg_btn(timeout).text

    def get_ft_expired_msg(self,timeout=5):
        wait = WebDriverWait(self.driver,timeout)
        return wait.until(EC.visibility_of_element_located(IDriveDashboardPage.ft_expired_msg))

    def get_ft_expired_msg_text(self,timeout=5):
        return self.get_ft_expired_msg(timeout).text

    def get_card_number(self,timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(IDriveDashboardPage.card_number))

    def get_card_expiry(self,timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(IDriveDashboardPage.card_expiry))

    def get_card_cvv(self):
        return self.driver.find_element(*IDriveDashboardPage.card_cvv)

    def get_bill_address(self,timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(IDriveDashboardPage.bill_address))

    def get_country_dropdown(self,timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(IDriveDashboardPage.country_dropdown))

    def get_state_dropdown(self,timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(IDriveDashboardPage.state_dropdown))

    def get_pin_code(self,timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(IDriveDashboardPage.pin_code))

    def get_check_box(self,timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(IDriveDashboardPage.check_box))

    def get_upgrade_button(self,timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(IDriveDashboardPage.upgrade_button))

    def update_plan_text_verify(self):
        try:
            self.get_upd_msg_btn_text()
            self.get_ft_expired_msg_text()
        except Exception as e:
            print(e)

    def update_plan_details(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            # 🔹 Wait for the iframe and switch to it
            iframe = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame']"))
            )
            self.driver.switch_to.frame(iframe)

            # 🔹 Fill card details
            wait.until(EC.element_to_be_clickable((By.NAME, "cardnumber"))).send_keys("4000 0566 5566 5556")
            wait.until(EC.element_to_be_clickable((By.NAME, "exp-date"))).send_keys("1230")
            wait.until(EC.element_to_be_clickable((By.NAME, "cvc"))).send_keys("455")

            # 🔹 Switch back to main content
            self.driver.switch_to.default_content()

            # 🔹 Fill billing info
            wait.until(EC.element_to_be_clickable((By.ID, "upgradeaddress"))).send_keys("Delhi")
            Select(wait.until(EC.element_to_be_clickable((By.NAME, "countryname")))).select_by_visible_text("India")
            #time.sleep(5)
            #Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@formcontrolname='state']")))).select_by_visible_text("Karnataka")
            time.sleep(10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Postal Code']"))).send_keys(
                "591002")

            # 🔹 Agree to terms and submit
            checkbox = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(@class,'id-checkmark')]")
                )
            )

            self.driver.execute_script("arguments[0].click();", checkbox)

            wait.until(EC.element_to_be_clickable((By.ID, "frm-btn1"))).click()

        except Exception as e:
            print("❌ Error in update_plan_details")
        traceback.print_exc()

    def get_current_url_end(self):
        return self.driver.current_url








