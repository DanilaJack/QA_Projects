from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
time.sleep(5)

#self keyword Xpath-axes
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Godrej Agrovet L')]/self::a").text
# print(text_msg)


#parent keyword Xpath-axes
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Godrej Agrovet L')]/parent::td").text
# print(text_msg)


#child keyword Xpath-axes
# childs = driver.find_elements(By.XPATH, "//a[contains(text(), 'Godrej Agrovet L')]/ancestor::tr/child::td")
# print(len(childs))  # 5 elements
# for child in childs:
#     print(child.text)
#
# driver.close()


#ancestor keyword Xpath-axes
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Godrej Agrovet L')]/ancestor::tr").text
# print(text_msg)
#
# driver.close()



#descendant keyword Xpath-axes
# descendants = driver.find_elements(By.XPATH, "//a[contains(text(), 'Godrej Agrovet L')]/ancestor::tr/descendant::*")
# print(len(descendants))
#
# driver.close()



#following keyword Xpath-axes
# followings = driver.find_elements(By.XPATH, "//a[contains(text(), 'Godrej Agrovet L')]/ancestor::tr/following::*")
# print(len(followings))
#
# driver.close()



#following-sibling keyword Xpath-axes
# followings_siblings = driver.find_elements(By.XPATH, "//a[contains(text(), 'Godrej Agrovet L')]/ancestor::tr/following-sibling::*")
# print(len(followings_siblings))
#
# driver.close()



#preceding keyword Xpath-axes
# precedings = driver.find_elements(By.XPATH, "//a[contains(text(), 'Godrej Agrovet L')]/ancestor::tr/preceding::tr")
# print(len(precedings))
#
# driver.close()


#preceding-sibling keyword Xpath-axes
preceding_siblings = driver.find_elements(By.XPATH, "//a[contains(text(), 'Godrej Agrovet L')]/ancestor::tr/preceding-sibling::tr")
print(len(preceding_siblings))


