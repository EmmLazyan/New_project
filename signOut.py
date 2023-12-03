import time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from pages_.navigationBar import NavigationBar
from tests_.baseTest import baseTestWithLogin

class SignOutPage(baseTestWithLogin):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())

    def test_sign_out_page(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_sign_out_element()
        time.sleep(6)
        self.assertEqual("Amazon Sign-In", self.driver.title)

    def tearDown(self):
        self.driver.close()