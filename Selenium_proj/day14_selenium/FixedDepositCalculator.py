import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from day14_selenium import XLUtils

serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/lakshmi-vilas-bank/fixed-deposit-calculator-LVB-BLV001.html")
driver.maximize_window()
time.sleep(3)


file = "C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/caldata.xlsx"
rows = XLUtils.getRowCount(file, "Sheet1")

for r in range(2, rows+1):

    # reading data from excel
    princ = XLUtils.readData(file, "Sheet1", r, 1)
    rateOfInt = XLUtils.readData(file, "Sheet1", r, 2)
    per1 = XLUtils.readData(file, "Sheet1", r, 3)
    per2 = XLUtils.readData(file, "Sheet1", r, 4)
    freq = XLUtils.readData(file, "Sheet1", r, 5)
    exp_mvalue = XLUtils.readData(file, "Sheet1", r, 6)

    #passing data to the app
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateOfInt)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)
    perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)
    freqdr = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    freqdr.select_by_visible_text(freq)
    driver.find_element(By.XPATH, "//div[@class='CTR PT15']/descendant::img[1]").click() # calculate button
    time.sleep(3)
    act_mvalue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    #Validation
    if float(exp_mvalue) == float(act_mvalue):
        print("test passed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Passed")
        XLUtils.fillGreenColor(file, "Sheet1", r, 8)
    else:
        print("test failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)


    #Cleaning of fields on the Web
    driver.find_element(By.XPATH, "//img[@class='PL5']").click()
    time.sleep(3)


driver.close()

