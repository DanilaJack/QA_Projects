import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://en.wikipedia.org/wiki/Software_testing")
driver.maximize_window()

#click on the link
# driver.find_element(By.LINK_TEXT, "History").click()
# time.sleep(3)


# find number of links in the page
# links = driver.find_elements(By.TAG_NAME, 'a')
# links = driver.find_elements(By.XPATH, '//a')
# print("Total number of links: ", len(links))

#print  all the link names
# for link in links:
#     print(link.text)
