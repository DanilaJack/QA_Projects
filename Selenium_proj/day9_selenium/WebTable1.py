# 1) count number of rows & columns
# 2) read specific row & column data
# 3) read all the rows & columns data
# 4) read data based on condition

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://theautomationzone.blogspot.com/2020/07/sample-webtable-3.html")
driver.maximize_window()
time.sleep(3)


# 1) count number of rows & columns
noOfRows = len(driver.find_elements(By.XPATH, "//table[@id='table1']/descendant::tr"))
noOfCols = len(driver.find_elements(By.XPATH, "//table[@id='table1']/descendant::tr[1]/th"))

print(noOfRows)
print(noOfCols)


# 2) read specific row & column data
data = driver.find_element(By.XPATH, "//table[@id='table1']//tr[6]/td[2]").text
print(data)
time.sleep(2)


# 3) read all the rows & columns data
# print("printing all the rows and columns data")
# for r in range(2, noOfRows+1):
#     for c in range(1, noOfCols+1):
#         data = driver.find_element(By.XPATH, f"//table[@id='table1']//tr[{r}]/td[{c}]").text
#         print(data, end='    ')
#     print()


# 4) read data based on condition - retrieve data with Jack lable in the cell of the table.
for r in range(2, noOfRows+1):
    FirstName = driver.find_element(By.XPATH, f"//table[@id='table1']//tr[{r}]/td[2]").text
    if FirstName == "Jack":
        Age = driver.find_element(By.XPATH, f"//table[@id='table1']//tr[{r}]/td[4]").text
        print(FirstName+"    "+Age)



driver.close()