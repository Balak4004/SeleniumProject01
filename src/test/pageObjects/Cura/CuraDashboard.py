from datetime import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v141.heap_profiler import take_heap_snapshot
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.test.utils.Utils import take_screenshot


class AppointmentDashboard:

    def __init__(self, driver):
        self.driver = driver

    #Page Locators
    facility_dropdown = (By.ID, "combo_facility")
    #facility_type = (By.XPATH,"//option[@value='Hongkong CURA Healthcare Center']")
    checkbox_readmission = (By.ID,"chk_hospotal_readmission")
    medicaid_radio_btn = (By.ID,"radio_program_medicaid")
    cal_element = (By.NAME,"visit_date")
    #month_yr_element = (By.XPATH,"//th[normalize-space()='November 2025']")
    #date_element = (By.XPATH,"//td[normalize-space()='17]")
    comment_box = (By.ID,"txt_comment")
    submit_btn = (By.ID,"btn-book-appointment")
    confirm_msg = (By.XPATH,"//h2[text()='Appointment Confirmation']")

    # Page Actions
    '''
    def get_facility_dropdown(self):
        return self.driver.find_element(*self.facility_dropdown)
    def get_facility_type(self):
        return self.driver.find_element(*self.facility_type)
    def get_checkbox_admission(self):
        return self.driver.find_element(*self.checkbox_admission)
    def get_medicaid_radio_btn(self):
        return self.driver.find_element(*self.medicaid_radio_btn)
    def get_cal_element(self):
        return self.driver.find_element(*self.cal_element)
    def get_month_yr_element(self):
        return self.driver.find_element(*self.month_yr_element)
    def get_date_element(self):
        return self.driver.find_element(*self.date_element)
    def get_comment_box(self):
        return self.driver.find_element(*self.comment_box)
    def get_submit_btn(self):
        return self.driver.find_element(*self.submit_btn)

'''
    def appointment_page(self,facility_name,visitdate,comment,timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            dropdown = wait.until(
                EC.presence_of_element_located(self.facility_dropdown)
            )

            select = Select(dropdown)
            select.select_by_visible_text(facility_name)
            wait.until(EC.element_to_be_clickable(self.checkbox_readmission)).click()
            wait.until(EC.element_to_be_clickable(self.medicaid_radio_btn)).click()
            date_input  = wait.until(EC.element_to_be_clickable(self.cal_element))
            date_input.clear()
            date_input.send_keys(visitdate)
            self.driver.find_element(By.TAG_NAME, "body").click()
            time.sleep(2)
            wait.until(EC.visibility_of_element_located(self.comment_box)).send_keys(comment)
            take_screenshot(driver=self.driver,name="appointment page")
            wait.until(EC.element_to_be_clickable(self.submit_btn)).click()
            time.sleep(3)
            take_screenshot(driver=self.driver, name="confirm page")
        except Exception as e:
            raise e

    def get_confirm_msg_text(self,timeout=10):
        wait = WebDriverWait(self.driver,timeout)
        return wait.until(EC.visibility_of_element_located(self.confirm_msg)).text


    def get_new_url(self):
        return self.driver.current_url
    #"https://katalon-demo-cura.herokuapp.com/appointment.php#summary"



