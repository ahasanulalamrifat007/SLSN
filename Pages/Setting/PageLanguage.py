import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class SelectLanguage:
    def enter_Language(self):
        element = self.driver.find_element("xpath", self.languageButton_xpath)
        element.click()
        time.sleep(5)
        # self.driver.find_element("xpath", self.languageSelect_xpath).send_keys("EN")