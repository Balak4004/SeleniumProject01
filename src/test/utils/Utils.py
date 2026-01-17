
import allure


def take_screenshot(driver,name):
    allure.attach(driver.get_screenshot_as_png(),name=name,attachment_type=allure.attachment_type.PNG)