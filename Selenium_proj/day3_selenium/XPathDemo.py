from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.tradeinn.com/goalinn/en")
driver.maximize_window() #maximize browser window
time.sleep(5)

#Absolute XPath
# driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[18]/div[2]/div[1]/div[1]/form[1]/input[1]").send_keys("T-shirts")
# time.sleep(5)


#Relative Xpath for the same element
# driver.find_element(By.XPATH, "//input[@type='search']").send_keys("T-shirts")
# time.sleep(3)


# Rel XPath with OR
# driver.find_element(By.XPATH, "//input[@type='search' or @autocomplete='off']").send_keys("T-shirt")
# time.sleep(3)


# Rel XPath with AND
# driver.find_element(By.XPATH, "//a[@class='navegation_ga firts_home' and @title='Boots']").click()
# time.sleep(5)


#contains()    &   starts-with()
# driver.find_element(By.XPATH, "//input[contains(@type,'search')]").send_keys("T-shirt")
# time.sleep(5)

# driver.find_element(By.XPATH, "//a[starts-with(@title,'Boots') and @class='navegation_ga firts_home']").click()
# time.sleep(5)


# text() function

# driver.find_element(By.XPATH, "//a[text()='Goalkeeper Gloves' and @class='navegation_ga firts_home']").click()
# time.sleep(5)

