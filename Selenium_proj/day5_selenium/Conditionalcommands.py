import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
time.sleep(15)

#is_displayed()  is_enabled()
search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("display_status", search_box.is_displayed())  #True
print("enable_status", search_box.is_enabled())   #True

#is_selected() - for radiobuttons and checkboxes mostly
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element((By.XPATH, "//input[@id='gender-female']"))

print(rd_male.is_selected())  # False
print(rd_female.is_selected())  #False

rd_male.click()

print("After selecting the male radio button....")
print(rd_male.is_selected())  # True
print(rd_female.is_selected())  #False

rd_female.click()

print("After selecting the female radio button....")
print(rd_male.is_selected())  # False
print(rd_female.is_selected())  #True


driver.quit()

