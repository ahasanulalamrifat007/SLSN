from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from getpass import getpass
from selenium.webdriver.chrome.service import Service
import time
from Pages.UAM.loginPage import Login
from Pages.CustomerAsset.AddFixedAsset import FixedAsset

'"""""""" Values  """"'
email = "fincentrumadmin@selise.ch"
password = "Helloworld@1"
# email = "qarifat30@gmail.com"
# password = "slsnAEIOU-1"
lang = "EN"
lang_c = "EN"
base_url = "https://stage-sln-fcsk.selise.biz/"
customer_id = "customers/b7bcdc9f-1f60-4770-9791-47ee771809ab/asset/fixed-asset"


'"""""""" Chrome Driver Setup  """"'
chrome_service = Service("C:\webdrivers\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()


'""""""""Driver initialize """"'
Login_page = Login(driver)
FixedAsset_page = FixedAsset(driver)


'"""""""" URL """"'
# driver.get(base_url+customer_id)
driver.get(base_url+customer_id)
time.sleep(10)

'"""""""" Executions """"'
Login_page.enter_Email(email)
time.sleep(2)
Login_page.enter_Password(password)
time.sleep(2)
Login_page.enter_Language(lang)
time.sleep(5)
Login_page.click_Login()
time.sleep(5)
print("Login Successful")
time.sleep(10)
""""" Add Fixed Asset """
FixedAsset_page.click_addasset()
time.sleep(10)
FixedAsset_page.select_vehicle()
FixedAsset_page.addTitle("Test Title")
FixedAsset_page.select_ownership()
FixedAsset_page.addValue("10000")
FixedAsset_page.click_confirm()
time.sleep(5)
print("Fixed Asset Added Successfully...")
time.sleep(10)
