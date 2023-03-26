from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from getpass import getpass
from selenium.webdriver.chrome.service import Service
import time
from Pages.UAM.loginPage import Login
from Pages.Contracts.Insurance import AddInsurance

'"""""""" Values  """"'
email = "fincentrumadmin@selise.ch"
password = "Helloworld@1"
lang = "EN"


'"""""""" Chrome Driver Setup  """"'
chrome_service = Service("C:\webdrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()

'""""""""Driver initialize """"'
Login_page = Login(driver)
Add_Insurance =AddInsurance(driver)

'"""""""" URL """"'
driver.get("http://sln-fcsk.seliselocal.com/customers/17c5f0d2-898e-479d-b824-fb4028aca48a/contracts/insure")
time.sleep(5)

'"""""""" Executions """"'
Login_page.enter_Email(email)
time.sleep(2)
Login_page.enter_Password(password)
time.sleep(2)
Login_page.enter_Language(lang)
time.sleep(5)
Login_page.click_Login()
print("Login Successful")
driver.implicitly_wait(10)
Add_Insurance.click_addInsurance()
time.sleep(20)

