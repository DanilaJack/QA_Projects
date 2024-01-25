import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0) # switch to the frame

#mm/dd/yyyy
# driver.find_element(By.ID, "datepicker").send_keys("05/15/2023")
# time.sleep(3)

year="2024"
month="November"
date="27"

driver.find_element(By.ID, "datepicker").click() #opens datepicker
time.sleep(2)

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        # driver.find_element(By.XPATH, "//a[@title='Prev']").click() #Prev arrow
        driver.find_element(By.XPATH, "//a[@title='Next']").click() #Next arrow

time.sleep(2)

# select date

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tr/td/a")

for el in dates:
    if el.text == date:
        el.click()
        break

time.sleep(3)
