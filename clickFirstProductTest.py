import time
from selenium import webdriver
from pages_.searchResultsPage import SearchResultsPage
from tests_.baseTest import baseTestWithoutLogin
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener

class search(baseTestWithoutLogin):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())

    def test_search_page(self):
        searchPageObj = SearchResultsPage(self.driver)
        searchPageObj.click_to_Search_Button()
        searchPageObj.click_to_The_first_product()
        time.sleep(10)

        self.assertNotEquals("Amazon.com : iphone", self.driver.title)

    def tearDown(self):
        self.driver.close()

