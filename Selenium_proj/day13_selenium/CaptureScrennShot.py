import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(3)

# driver.save_screenshot(os.getcwd()+"/homepage.png")

# driver.get_screenshot_as_file(os.getcwd()+"/homepage.png")

# driver.get_screenshot_as_png(os.getcwd()+"/homepage.png")   saves in binary format
# driver.get_screenshot_as_base64(os.getcwd()+"/homepage.png")  saves in binary format


driver.quit()
