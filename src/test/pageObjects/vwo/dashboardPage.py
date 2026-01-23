
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.test.utils.common_utils import *


class DashboardPage:

    def __init__(self,driver):
        self.driver = driver

    user_logged_in = (By.XPATH,"//h6[@class='Fw(medium) Mb(0) Mend(4px) Mend(0):lc ng-binding ellipsis']")
    user_logged_in_id = (By.XPATH,"//span[@class='badge badge--small text-monospaced Fxs(0) Mend(4px) Mend(0):lc']")

    # Page Actions
    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    def user_logged_in_text(self,timeout=20):
        wait = WebDriverWait(self.driver,timeout)
        wait.until(EC.visibility_of_element_located(self.user_logged_in))
        return self.get_user_logged_in().text
