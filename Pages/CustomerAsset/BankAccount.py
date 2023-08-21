from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class BankAccount:
    def __init__(self, driver):
        self.driver = driver
        self.addbankButton_xpath = '//button/span[text()=" Add Bank Account "]'
        self.title_xpath = '//input[@formcontrolname="Title"]'
        self.ibanNumber_xpath = '//input[@formcontrolname="IBANNo"]'
        self.bic_xpath = '//input[@formcontrolname="BIC"]'

    def click_addBank(self):
        time.sleep(10)
        self.driver.find_element("xpath", self.addbankButton_xpath).click()
    def add_title(self, title):
        time.sleep(5)
        self.driver.find_element("xpath", self.title_xpath).send_keys(title)
    def add_IBANNo(self, no):
        time.sleep(5)
        self.driver.find_element("xpath", self.ibanNumber_xpath).send_keys(no)
    def add_bic(self, bic):
        time.sleep(5)
        self.driver.find_element("xpath", self.bic_xpath).send_keys(bic)
