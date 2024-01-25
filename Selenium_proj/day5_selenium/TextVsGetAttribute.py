import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.orangehrm.com/")
driver.maximize_window()
time.sleep(3)

emailbox = driver.find_element(By.ID, "Form_submitForm_EmailHomePage")
emailbox.clear()
emailbox.send_keys("abc@gmail.com")
time.sleep(3)

print("result of the text: ", emailbox.text)   #print nothing
print("result of the get_attribute(): ", emailbox.get_attribute('value'))  #print value attribute

button = driver.find_element(By.XPATH, "//div[@class='d-flex web-menu-btn']//li[1]//a[1]")
print("result of the text: ", button.text)
print("result of the get_attribute(): ", button.get_attribute('value'))