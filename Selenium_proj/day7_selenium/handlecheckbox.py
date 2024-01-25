import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://artoftesting.com/samplesiteforselenium")
# driver.maximize_window()

# 1) select specific checkbox from the list
# driver.find_element(By.XPATH, "//input[@value='Automation']").click()
# time.sleep(3)

# 2) select all the checkboxes
# check_boxes = driver.find_elements(By.XPATH, "(//form[normalize-space()='Automation Testing Performance Testing']//input)")
# print(len(check_boxes))

# # check_boxes[0].click()
# # check_boxes[1].click()
#
# for check_box in check_boxes:
#     check_box.click()
# time.sleep(3)


# 3) select some checkboxes by choice

# for check_box in check_boxes:
#     poss_check = check_box.get_attribute('value')
#     if poss_check == "Performance":
#         check_box.click()


# 4) select some amount of last checkboxes:

driver.get("https://faculty.washington.edu/chudler/java/boxes.html")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

# so now I want to check last and pre-last checkboxes that's why I specify this range
# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click()
# time.sleep(2)

# 5) select several first checkboxes

# for i in range(3):
#     checkboxes[i].click()
#
# time.sleep(3)


# 6) clearing all the checkboxes

for checkbox in checkboxes:
    checkbox.click()

time.sleep(3)

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

time.sleep(3)