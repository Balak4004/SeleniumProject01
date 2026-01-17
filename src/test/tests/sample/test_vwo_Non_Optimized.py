
import pytest
import allure
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from src.test.utils.Utils import take_screenshot

@allure.title("Vwo Login Negative test case")
@allure.description("TC#1 Negative test case - Login with invalid credentials")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    match os.getenv("BROWSER"):
        case "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(options=chrome_options)

        case "edge":
            edge_options = Options()
            edge_options.add_argument("--inprivate")
            driver = webdriver.Edge(options=edge_options)

        case _:
            print("Browser not found")
            exit(1)

    driver.get(os.getenv("URL"))
    driver.maximize_window()
    time.sleep(2)
    
    take_screenshot(driver=driver,name="vwo_login_step_1")



    Email_address_element = driver.find_element(By.ID, "login-username")
    Email_address_element.click()
    Email_address_element.send_keys(os.getenv("INVALID_USERNAME"))
    time.sleep(1)

    Password_element = driver.find_element(By.ID, "login-password")
    Password_element.click()
    Password_element.send_keys(os.getenv("INVALID_PASSWORD"))
    time.sleep(1)

    sign_in_button = driver.find_element(By.ID, "js-login-btn")
    sign_in_button.click()
    time.sleep(4)

    error_msg = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_msg.text)

    take_screenshot(driver=driver, name="vwo_login_step_2")

    assert error_msg.text == os.getenv("error_message_expected")

    time.sleep(2)
    driver.quit()








