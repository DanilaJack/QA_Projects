import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-CUHVHGM\SQLEXPRESS'
DATABASE_NAME = 'Employee'
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""


serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/lakshmi-vilas-bank/fixed-deposit-calculator-LVB-BLV001.html")
driver.maximize_window()
time.sleep(3)


try:
    con = odbc.connect(connection_string)  # generates the connection between ms sql server and python env.

    curs = con.cursor()  # create cursor
    curs.execute("select * from caldata")  # execute query through cursor


    for row in curs:

        # reading data from db
        princ = row[0]
        rateOfInt = row[1]
        per1 = row[2]
        per2 = row[3]
        freq = row[4]
        exp_mvalue = row[5]

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
        else:
            print("test failed")


        #Cleaning of fields on the Web
        driver.find_element(By.XPATH, "//img[@class='PL5']").click()
        time.sleep(3)

    con.close()

except:
    print("Connection unsuccessful")

driver.close()
