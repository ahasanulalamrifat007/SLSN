from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from getpass import getpass
import time
class Login:
    '''''''"Veriable Declaration"'''
    def __init__(self, driver):
        self.driver = driver
        self.email_xpath = '//input[@name="email"]'
        self.password_xpath = '//input[@name="password"]'
        self.languageSelect_xpath = '//div/mat-select[@name="language"]'
        self.loginButton_xpath = '//button[@aria-label="LOGIN"]'

    '''''''"Execution"'''

    def enter_Email(self, Email):
        self.driver.find_element("xpath", self.email_xpath).send_keys(Email)

    def enter_Password(self, Password):
        self.driver.find_element("xpath", self.password_xpath).send_keys(Password)

    def enter_Language(self, Language):
        self.driver.find_element("xpath", self.languageSelect_xpath).send_keys(Language)

    def click_Login(self):
        self.driver.find_element("xpath", self.loginButton_xpath).click()



