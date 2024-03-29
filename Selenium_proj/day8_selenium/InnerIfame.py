import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

outter_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outter_frame)

inner_frame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)

driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("Welcome")
driver.switch_to.parent_frame() # directly switch to parent frame (outter_frame)
time.sleep(5)