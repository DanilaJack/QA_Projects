from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window() #maximize browser window
time.sleep(10)

sliders = driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(sliders))

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))
