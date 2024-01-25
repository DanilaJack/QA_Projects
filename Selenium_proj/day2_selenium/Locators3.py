from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)

#tag&id
#driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, '#email').send_keys("abc")
# time.sleep(5)


#tag&class
#driver.find_element(By.CSS_SELECTOR, "input.inputtext._55r1._6luy").send_keys("abc@gmail.com")  # here's the example with multiple classes
#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, ".inputtext._55r1._6luy").send_keys("abc@gmail.com")
# time.sleep(5)


#tag&attribute
#driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc@gmail.com")
# time.sleep(5)


#tag, class & attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("xyz")
time.sleep(4)

