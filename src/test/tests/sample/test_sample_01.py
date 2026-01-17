
import pytest
import allure
import time

@allure.title("Dry run of pass test case")
@allure.description("TC#1 Dry run of pass test case")
def test_sample_pass():
    print("Hi")
    assert True == True

@allure.title("Dry run of fail test case")
@allure.description("TC#2 Dry run of fail test case")
def test_sample_fail():
    print("Hi")
    assert True == False