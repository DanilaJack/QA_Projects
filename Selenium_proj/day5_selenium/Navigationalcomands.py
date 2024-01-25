from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/")

driver.back()   # browser goes back to the snapdeal (it's like click on arrow <- )
driver.forward()  # browser goes forward to the amazon (it's like click on arrow -> )

driver.refresh()  # just reloading the page

driver.quit()