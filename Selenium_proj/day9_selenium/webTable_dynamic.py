import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(3)

#Login
driver.find_element(By.NAME, "username").send_keys("Admin")
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")
password.submit()
time.sleep(5)

#Admin - User Management - User
driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']/li[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click()
time.sleep(3)

#Total rows in a table
rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div"))
print("total number of rows in a table: ", rows)

count = 0
for r in range(1, rows+1):
    status = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[5]").text
    if status == "Enabled":
        count += 1

print("number of enabled users: ", count)
print("number of disabled users: ", rows-count)




