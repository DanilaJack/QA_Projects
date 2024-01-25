import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(3)

# # every time when I launch the browser - id will be different
# windowid = driver.current_window_handle
# print(windowid)  # 391210F7D4076F1B323091F646FB75E4


driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
# to get window id's of both windows
windowIDs = driver.window_handles

# Approach1 - if we have one, two, three browser windows
# parentwindowid = windowIDs[0]  #9A08C325CCBE670521C1039CFA9AEAB8
# childwindowid = windowIDs[1]  #D8606CA5A531C66C21B490B05165817A

#print(parentwindowid, childwindowid)

# driver.switch_to.window(childwindowid)
# print("title of the child window: " + driver.title)
# time.sleep(3)
#
# driver.switch_to.window(parentwindowid)
# print("title of the parent window: " + driver.title)
# time.sleep(3)

# Approach 2 - loop statement

# for winid in windowIDs:
#     driver.switch_to.window(winid)
#     print(driver.title)


for winid in windowIDs:  # first we specify all the browser windows
    driver.switch_to.window(winid)    # and based on certain condition we perform some actions we want
    if driver.title == "OrangeHRM HR Software | OrangeHRM" or driver.title == "XYZ":   # in this case we simply close window
        driver.close()

time.sleep(3)