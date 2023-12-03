import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from testData_.testData import validUser, userWithInvalidPassword, mainPageUrl, signInPageUrl
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class baseTestWithoutLogin(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(mainPageUrl)

    def tearDown(self):
        self.driver.close()

class baseTestWithLogin(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(signInPageUrl)
        testValue= False
        message = "There was a problem. Your password is incorrect"
        logInPageObj= LoginPage(self.driver)
        logInPageObj.fill_username_field(validUser.username)
        logInPageObj.click_on_continue_button()
        logInPageObj.fill_password_field(userWithInvalidPassword.password)
        logInPageObj.click_on_signin_button()
        time.sleep(10)
        self.assertFalse(testValue, message)

    def tearDown(self):
        self.driver.close()
