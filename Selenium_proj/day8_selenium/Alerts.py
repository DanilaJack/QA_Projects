import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#opens alert window
driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
time.sleep(2)

alertwindow = driver.switch_to.alert

print(alertwindow.text)  # text in this pop-up/alert window
alertwindow.send_keys("welcome")  # placing some text into the input field pf this alert window
# alertwindow.accept()   # close alert window by clicking ok
alertwindow.dismiss()    # close alert window by clicking cancel
time.sleep(3)

