import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.orangehrm.com/")
driver.maximize_window()
time.sleep(5)

#############    find_element() - return single web-element

# 1) Locator matching with single web element
# element = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_EmailHomePage']")
# element.send_keys("Apple Mac Book")
# time.sleep(3)

# 2) Locator matching with multiple web elements
# element = driver.find_element(By.XPATH, "//div[@class='footer-main-section']//a")
# print(element.text)
# time.sleep(5)  #prints first link from 20 found elements - OrangeHRM

# 3) Element not available then throw NoSuchElementException

# book_element = driver.find_element(By.XPATH, "//div[@type='d-flex web-menu-btn']//li[1]//a[1]")
# book_element.click()



########## find_elements() - return multiple web-elements

# 1) Locator matching with single web-element
# elements = driver.find_elements(By.XPATH, "//input[@id='Form_submitForm_EmailHomePage']")
# # here although it's a single element it's been written as a list of elements
# print(len(elements)) #1
#
# elements[0].send_keys("Apple Mac Book")


# 2) Locator matching with multiple web-elements

# elements = driver.find_elements(By.XPATH, "//div[@class='footer-main-section']//a")
# print(len(elements))
# print(elements[5].text)
# for item in elements:
#     print(item.text)



# 3) Element not available then.... it'll return zero, but no exceptions.

elements = driver.find_elements(By.XPATH, "//div[@type='d-flex web-menu-btn']//li[1]//a[1]")
print("elements returned: ", len(elements))