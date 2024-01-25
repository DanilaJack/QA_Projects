from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window() #maximize browser window
time.sleep(10)

# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")


#linkText & PartialLinkText

driver.find_element(By.LINK_TEXT, "Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()  #Just a part of the whole text

#driver.close()
#driver.quit()




