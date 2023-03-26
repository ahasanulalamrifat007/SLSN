from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class AddInsurance:
    '''''''"Veriable Declaration"'''
    def __init__(self,driver):
        self.driver = driver
        # self.addButton_xpath = '//button[@aria-label="Add insurance contract"]'
        self.addButton_xpath = '//button/span[text()=" Add Insure Contract "]'



    def click_addInsurance(self):
        # print("Element is visible? " + str(self.addButton_xpath.is_displayed()))
        self.driver.find_element("xpath", self.addButton_xpath).click()

