from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from getpass import getpass
from selenium.webdriver.chrome.service import Service
import time
from Pages.UAM.loginPage import Login
from Pages.Contracts.Insurance import AddInsurance

'"""""""" Values  """"'
# email = "fincentrumadmin@selise.ch"
# password = "Helloworld@1"
email = "95000125@yopmail.com"
password = "1qazZAQ!"
lang = "EN"
base_url="http://sln-fcsk.seliselocal.com"
customer_id="customers/68785339-f152-4749-9c1f-41e79d1e9ba1/"


'"""""""" Chrome Driver Setup  """"'
chrome_service = Service("C:\webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()

'""""""""Driver initialize """"'
Login_page = Login(driver)
Add_Insurance =AddInsurance(driver)

'"""""""" URL """"'
# driver.get(base_url+customer_id)
driver.get(base_url)
time.sleep(5)

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

driver.get(base_url+"/contracts/insure")
time.sleep(10)
Add_Insurance.click_addInsurance()
time.sleep(20)

