import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.orangehrm.com/")
driver.maximize_window()

# Needed elements for moving to them (hovering them)
Resourses = driver.find_element(By.XPATH, "//a[@class='nav-link-hed'][normalize-space()='Resources']")
Product_overview = driver.find_element(By.XPATH, "//div[@class='secondary secondary-menu-2']//li[3]")
OrangeProduct = driver.find_element(By.XPATH, "//h6[@class='list-sub-menu-title']//a[normalize-space()='OrangeHRM ROI']")


#MouseHover

act = ActionChains(driver)
act.move_to_element(Resourses).move_to_element(Product_overview).move_to_element(OrangeProduct).click().perform()
time.sleep(3)