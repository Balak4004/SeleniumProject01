
from selenium import webdriver
from selenium.webdriver import Chrome
import pytest

import os
from dotenv import load_dotenv
load_dotenv()



@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()

#@pytest.fixture(scope='class')
#def setup(request):
    #driver.maximize_window()
    #username = os.getenv("INVALID_USERNAME")
    #password = os.getenv("INVALID_PASSWORD")

    #request.cls.driver = driver
    #request.cls.username = username
    #request.cls.password = password

    yield driver
    driver.quit()
