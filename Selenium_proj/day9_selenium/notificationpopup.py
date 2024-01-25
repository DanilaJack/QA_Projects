import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# to get rid off some notifications pop-ups we create ops object
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=ops)  # pass service and created ops object

driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(3)