import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)
# driver.close()
driver.quit()
time.sleep(10)
