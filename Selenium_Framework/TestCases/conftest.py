import os.path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as SC
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.edge.service import Service as SE


@pytest.fixture(scope="function")
def setup(request, browser, url):

    if browser == "chrome":
        srv_obj = SC("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/chromedriver.exe")
        global driver
        driver = webdriver.Chrome(service=srv_obj)

    elif browser == "firefox":
        srv_obj = SF("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/geckodriver.exe")
        driver = webdriver.Firefox(service=srv_obj)

    elif browser == "edge":
        srv_obj = SE("C:/Users/danil/Desktop/automated_testing/Selenium Web Automation/SeleniumPython_PavanCourse/WebDrivers/msedgedriver.exe")
        driver = webdriver.Edge(service=srv_obj)

    driver.get(url)
    # "https://www.yatra.com/"
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()



def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        extra.append(pytest_html.extras.url("https://www.google.com/"))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):

            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            _capture_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(destination_file):
    driver.get_screenshot_as_file(destination_file)


def pytest_html_report_title(report):
    report.title = "Automation Report"


