# Test case
# ----------------
# 1) Open Web Browser (Chrome/Firefox/Edge)
# 2) Open URL( https://opensource-demo.orangehrmlive.com/ )
# 3) Enter username (Admin)
# 4) Enter password (admin123)
# 5) Click on Login
# 6) Capture title of the home page. (Actual title)
# 7) Verify title of the page: OrangeHRM        (Expected)
# 8) Close Browser

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)


driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(5)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
time.sleep(5)
act_title = driver.title
exp_title = "OrangeHRM"


if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")


driver.close()



