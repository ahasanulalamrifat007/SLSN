import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AddInsurance:
    '''''''"Veriable Declaration"'''
    def __init__(self,driver):
        self.driver = driver
        self.addButton_xpath = '//button/span[text()=" Add Insure Contract "]'
        # self.addButton_xpath = '//button[@aria-label="Add insure contact"]'



    def click_addInsurance(self):
        # print("Element is visible? " + str(self.addButton_xpath.is_displayed()))
        time.sleep(15)
        self.driver.find_element("xpath", self.addButton_xpath).click()
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.addButton_xpath))).click()

