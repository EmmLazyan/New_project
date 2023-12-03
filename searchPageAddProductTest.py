import time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from pages_.searchResultsPage import SearchResultsPage
from tests_.baseTest import baseTestWithLogin

class add_new_product(baseTestWithLogin):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())

    def test_add_new_product(self):
        searchResultsPageObj = SearchResultsPage(self.driver)
        searchResultsPageObj._fill_Search_Field("christmas gifts")
        searchResultsPageObj.click_To_Search_Button()
        searchResultsPageObj.click_to_result_element()
        searchResultsPageObj.click_to_add_button()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()
