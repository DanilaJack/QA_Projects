import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.google.com/")
driver.implicitly_wait(10)  # 10 seconds
driver.maximize_window()

searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
searchbox.submit()

driver.find_element(By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][text()='Selenium']").click()

