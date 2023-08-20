import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from getpass import getpass

class FixedAsset:
    def __init__(self, driver):
        self.driver = driver
        self.addAsset_xpath = '//button/span/span[text()=" Add Fixed Asset "]'
        self.confirmButton_xpath = '//button/span[text()=" Confirm "]'
        self.vehicleSelect_xpath = '//button/span/div/div[2]/p[text()=" Vehicle "]'
        self.landSelect_xpath = '//button/span/div/div[2]/p[text()=" Land "]'
        self.propertySelect_xpath = '//button/span/div/div[2]/p[text()=" Property "]'
        self.valuablesSelect_xpath = '//button/span/div/div[2]/p[text()=" Valuables "]'
        self.othersSelect_xpath = '//button/span/div/div[2]/p[text()=" Others "]'
        self.othersSelect_xpath = '//button/span/div/div[2]/p[text()=" Others "]'
        self.title_xpath = '//input[@data-placeholder="Title"]'
        self.value_xpath = '//input[@data-placeholder="Value (EUR)"]'
        self.ownnership_xpath = '//label/span[2][text()=" Sole "]'



    def click_addasset(self):
        time.sleep(10)
        self.driver.find_element("xpath", self.addAsset_xpath).click()
    def select_vehicle(self):
        time.sleep(10)
        self.driver.find_element("xpath", self.vehicleSelect_xpath).click()
    def addTitle(self, Title):
        time.sleep(10)
        self.driver.find_element("xpath", self.title_xpath).send_keys(Title)
    def select_ownership(self):
        time.sleep(10)
        self.driver.find_element("xpath", self.ownnership_xpath).click()
    def addValue(self, Value):
        time.sleep(10)
        self.driver.find_element("xpath", self.value_xpath).send_keys(Value)
    def click_confirm(self):
        time.sleep(5)
        self.driver.find_element("xpath", self.confirmButton_xpath).click()


