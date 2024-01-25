from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
    ops = webdriver.ChromeOptions()
    # ops.headless = True
    ops.add_argument('--headless=new')

    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver


def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/msedgedriver.exe")
    ops = webdriver.EdgeOptions()
    # ops.headless = True
    ops.add_argument('--headless=new')

    driver = webdriver.Edge(service=serv_obj, options=ops)
    return driver


def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/geckodriver.exe")
    ops = webdriver.FirefoxOptions()
    # ops.headless = True
    ops.add_argument('-headless')

    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver


# driver = headless_chrome()
# driver = headless_edge()
driver = headless_firefox()

driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.close()