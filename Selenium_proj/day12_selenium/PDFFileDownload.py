import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd() # get current working directory

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")

    # download files in disered location
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)  # desired location for downloading
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver


def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/msedgedriver.exe")

    # download files in disered location
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)  # desired location for downloading
    driver = webdriver.Edge(service=serv_obj, options=ops)
    return driver



def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/geckodriver.exe")

    #settings
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2) # 0 - desktop, 1- downloads, 2 - desired location
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True)  # for pdf


    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver


#Automation code
# driver = chrome_setup()
# driver = edge_setup()

driver = firefox_setup()
driver.implicitly_wait(10)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
dwnl_file = driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]")
driver.execute_script("window.scrollBy(0,500)", "")
dwnl_file.click()
time.sleep(20)
driver.close()