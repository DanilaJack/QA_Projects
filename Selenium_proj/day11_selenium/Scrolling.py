import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()


# 1. Scroll down the page by pixel

# driver.execute_script("window.scrollBy(0,3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved: ", value)
# time.sleep(2)


# 2. Scroll down the page till element is visible

# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved: ", value)
# time.sleep(2)


# 3. Scroll down the page till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)


# Scroll up to the starting position
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)") # here I put - sign before document....
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", value)
time.sleep(3)