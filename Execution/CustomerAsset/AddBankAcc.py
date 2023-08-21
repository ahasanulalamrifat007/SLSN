from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import time
from Pages.UAM.loginPage import Login
from Pages.CustomerAsset.BankAccount import BankAccount

'"""""""" Values  """"'
email = "fincentrumadmin@selise.ch"
password = "Helloworld@1"
# email = "qarifat30@gmail.com"
# password = "slsnAEIOU-1"
lang = "EN"
lang_c = "EN"
base_url = "https://stage-sln-fcsk.selise.biz/"
customer_id = "customers/b7bcdc9f-1f60-4770-9791-47ee771809ab"
extension = "/asset/bank-account"


'"""""""" Chrome Driver Setup  """"'
chrome_service = Service("C:\webdrivers\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()


'""""""""Driver initialize """"'
Login_page = Login(driver)
BankAccount_page = BankAccount(driver)


'"""""""" URL """"'

driver.get(base_url+customer_id+extension)
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
""""" Add Bank Acc """
BankAccount_page.click_addBank()
time.sleep(10)
BankAccount_page.add_title("Automated Added Acc")
time.sleep(5)
BankAccount_page.add_IBANNo("31 8123 9000 0012 4568 2232")
time.sleep(5)
BankAccount_page.add_bic("AZBXAT52")
time.sleep(5)