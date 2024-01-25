import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Base.base_driver import BaseDriver
from Pages.search_flights_results_page import SearchFlightsResults
from Utilities.utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    SELECT_DATE_LIST = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' and @class!='inActiveTD weekend']"
    SEARCH_FLIGHTS_BUTTON = "//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getDepartureDateField(self):
        return self.driver.find_element(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesList(self):
        return self.driver.find_elements(By.XPATH, self.SELECT_DATE_LIST)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_FLIGHTS_BUTTON)


    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        self.log.info("user clicked on the field")
        time.sleep(2)
        self.getGoingToField().send_keys(goingtolocation)
        self.log.info("user typed text successfully")
        search_results = self.getGoingToResults()
        for results in search_results:
            time.sleep(1)
            if goingtolocation in results.text:
                results.click()
                break


    def enterDepartureDate(self, departuredate):
        time.sleep(1)
        self.getDepartureDateField().click()
        time.sleep(2)
        all_dates = self.getAllDatesList()
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                time.sleep(3)
                break


    def clickSearchFlightsButton(self):
        self.getSearchButton().click()
        time.sleep(4)


    def SearchFlights(self, departurelocation, goingtolocation, departuredate):
        self.enterDepartFromLocation(departurelocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        self.clickSearchFlightsButton()
        search_flight_result = SearchFlightsResults(self.driver)
        return search_flight_result
