
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.test.constants.Constants import Constants

# Method overloading
def webdriver_wait(driver, element_tuple, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(element_tuple)
    )


def webdriver_wait_1(driver,element_tuple,timeout):
    WebDriverWait(driver=driver,timeout=timeout).until(EC.visibility_of_element_located(element_tuple))

def webdriver_wait_url(driver,timeout):
    WebDriverWait(driver=driver,timeout=timeout).until(EC.url_changes(Constants.app_dashboard_url()))

'''
