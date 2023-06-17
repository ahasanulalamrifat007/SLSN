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
email = "qarifat30@gmail.com"
password = "slsnAEIOU-1"
lang = "EN"
lang_c = "EN"
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
# print("Which type of Contracts you want to create- \n 1.Insurance \n 2.Loan \n 3.Retirement \n 4.Investment \n 5.Others" )
# time.sleep(10)
# print("Enter Number -- ")
# contract_name = int(input())

driver.get(base_url+"/contracts/insure")
time.sleep(20)
Add_Insurance.enter_Language()
time.sleep(20)
# Add_Insurance.click_addInsurance()
# time.sleep(20)








# """Customer End Contract Create Start"""
# if contract_name == 1:
#     driver.get(base_url+"/contracts-new/insure")
#     time.sleep(10)
#     Add_Insurance.click_addInsurance()
#     time.sleep(20)
# elif contract_name == 2:
#     driver.get(base_url+"/contracts/loan")
#     time.sleep(10)
# elif contract_name == 3:
#     driver.get(base_url+"/contracts/retirement")
#     time.sleep(10)
# elif contract_name == 4:
#     driver.get(base_url+"/contracts/investmentContract")
#     time.sleep(10)
# elif contract_name == 5:
#     driver.get(base_url+"/contracts/other-contract")
#     time.sleep(10)
# else:
#     print("Enter Wrong Number")
#     time.sleep(5)


#driver.implicitly_wait(10)
# Add_Insurance.click_addInsurance()
# time.sleep(20)

