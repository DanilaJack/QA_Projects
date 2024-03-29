import logging
import time

from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Utilities.utils import Utils


class SearchFlightsResults(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FILTER_BY_1_STOP_ICON = "//p[normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]"

    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_none_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)

    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            self.log.warning("Selected flights with one stop")
            time.sleep(2)

        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            self.log.warning("Selected flights with two stops")
            time.sleep(2)

        elif by_stop == "Non Stop":
            self.get_filter_by_none_stop_icon().click()
            self.log.warning("Selected flights without stops")
            time.sleep(2)

        else:
            self.log.warning("Provide valid filter option")


