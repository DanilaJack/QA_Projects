import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

act = ActionChains(driver)

source_el = driver.find_element(By.ID, "box6")
target_el = driver.find_element(By.ID, "box106")
act.drag_and_drop(source_el, target_el).perform()  # drag source el and drop it into target el
time.sleep(3)

wash_el = driver.find_element(By.ID, "box3")
usa_el = driver.find_element(By.ID, "box103")
act.drag_and_drop(wash_el, usa_el).perform()  # drag source el and drop it into target el
time.sleep(3)