import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)

# Web Driver Application-related commands
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()