import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@class='heroSection-buttonContainer_secondaryBtn__text']").click()
time.sleep(5)
driver.find_element(By.ID, "file-upload").send_keys("C:/Users/danil/Desktop/automated_testing/API's testing/files/store.txt")
time.sleep(5)
