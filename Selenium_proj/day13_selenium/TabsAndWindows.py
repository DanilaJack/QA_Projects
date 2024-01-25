import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://quizlet.com/153920048/chapter-4-flash-cards/")
# driver.maximize_window()

# Solution_option = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Решения от экспертов").send_keys(Solution_option)
# time.sleep(3)


#New tab - selenium4: opens a new tab at the same window and switches to it
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.orangehrm.com/")
# time.sleep(3)

# New tab - selenium4: opens a new browser window and switches to it
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")
time.sleep(3)
