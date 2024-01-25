import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://automationtesting.co.uk/dropdown.html")
driver.maximize_window()

drpcars_el = driver.find_element(By.XPATH, "//select[@id='cars']")
drpcars = Select(drpcars_el)

# select option from the drop-drown

#drpcars.select_by_visible_text("BMW")
# drpcars.select_by_value("ford")
# drpcars.select_by_index(5)
# time.sleep(5)


# capture all the options from the drop-down and print

alloptions = drpcars.options
print("Total number of options: ", len(alloptions))

# for option in alloptions:
#     print(option.text)


# select option from drop-down without using buil-in functions (select_by_value)


for option in alloptions:
    if option.text == "BMW":
        option.click()
        break

time.sleep(3)
