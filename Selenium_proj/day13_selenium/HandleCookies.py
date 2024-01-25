import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

#Capture cookies from the browser
cookies = driver.get_cookies()
print("Size of cookies: ", len(cookies)) #3

#Print details of all cookies created by browser
# for c in cookies:
#     print(c.get('name'), ": ", c.get('value'))


# Add new cookie to the browser
driver.add_cookie({"name": "MyCookie", "value": "123456"})
cookies = driver.get_cookies()
print("Size of cookies after appending new one: ", len(cookies))  #4


# delete a specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("Size of cookies after deleting one: ", len(cookies)) #3


#Delete all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of cookies after deleting all cookies: ", len(cookies)) #3



driver.quit()
