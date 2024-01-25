import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
# driver.maximize_window()
# time.sleep(5)
#
# driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
# driver.find_element(By.LINK_TEXT, "WebDriver").click()
#
# driver.find_element(By.XPATH, "//a[normalize-space()='Help']").click()
# time.sleep(3)

driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()

driver.switch_to.frame(0)
driver.find_element(By.XPATH, "//input[@name='mytext1']").send_keys("Welcome")
driver.switch_to.default_content()

driver.switch_to.frame(1)
driver.find_element(By.XPATH, "//input[@name='mytext2']").send_keys("Welcome")
driver.switch_to.default_content()

driver.switch_to.frame(2)
driver.find_element(By.XPATH, "//input[@name='mytext3']").send_keys("Welcome")
driver.switch_to.default_content()
time.sleep(3)

