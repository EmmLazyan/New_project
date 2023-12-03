import time
from selenium import webdriver
from pages_.navigationBar import NavigationBar
from tests_.baseTest import baseTestWithoutLogin
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class navigationBar(baseTestWithoutLogin):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())

    def test_navigation_bar_page(self):
     navigationBarObj = NavigationBar(self.driver)
     navigationBarObj.click_to_go_to_homepage_button()

     time.sleep(10)

     self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

    def tearDown(self):
        self.driver.close()