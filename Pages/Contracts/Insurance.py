import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AddInsurance:
    '''''''"Veriable Declaration"'''
    def __init__(self,driver):
        self.driver = driver
        self.languageButton_xpath = '//button[@class="mat-focus-indicator mat-menu-trigger language-button mat-button mat-button-base"]'
        self.languageSelect_xpath = '//button/span/div/span[@class="iso font-size-16 text-uppercase"]'
        self.addButton_xpath = '//button[@aria-label="Add insure contact"]'
        # self.addButton_xpath = '//button/span[text()= " Add Insure Contract " ]'
        # self.addButton_xpath = '//button/span/mat-icon[@class="mat-icon notranslate font-size-20 w-20 line-height-18 h-20 mr-4 material-icons mat-icon-no-color" ]'
        # self.addButton_xpath = '//button/span[text()= " Pridať poistnú zmluvu "]'


    def enter_Language(self):
        element = self.driver.find_element("xpath", self.languageButton_xpath)
        element.click()
        time.sleep(5)
        # self.driver.find_element("xpath", self.languageSelect_xpath).send_keys("EN")


    def click_addInsurance(self):
        time.sleep(10)
        self.driver.find_element("xpath", self.addButton_xpath).click()

        # ActionChains(self.driver).click(add).perform()
        # ActionChains(self.driver).move_to_element(add).click(add)

        # add=self.driver.find_element("xpath", self.addButton_xpath)
        # add.click()
        # # assert el.text == "Add Insure Contract"

        # print(self.driver.find_element("xpath", self.addButton_xpath))
        # self.driver.find_element("xpath", self.addButton_xpath).click()
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.addButton_xpath))).click()

