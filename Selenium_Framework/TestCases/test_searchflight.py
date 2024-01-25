import softest
import pytest
from Pages.yatra_launch_page import LaunchPage
from Utilities.utils import Utils
from ddt import ddt, data, file_data, unpack



@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()

    # @file_data("../TestData/testdata.json")
    #@data(*Utils.read_data_from_excel("C:\\Users\\danil\\Desktop\\automated_testing\\Selenium Web Automation\\Newfolder\\Framework2\\TestData\\testData.xlsx", "Data"))
    #@unpack
    @data(*Utils.read_data_from_csv("C:\\Users\\danil\\Desktop\\automated_testing\\Selenium Web Automation\\Newfolder\\Framework2\\TestData\\tdatacsv.csv"))
    @unpack
    def test_search_flights_1_stop(self, goingfrom, goingto, date, stops):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()
        search_flight_results = self.lp.SearchFlights(goingfrom, goingto, date)
        self.lp.pageScroll()
        search_flight_results.filter_flights_by_stop(stops)
        allstops1 = search_flight_results.get_search_flight_results()
        self.log.info(len(allstops1))
        self.ut.assertListItemsText(allstops1, stops)


