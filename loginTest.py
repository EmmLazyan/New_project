import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from testData_.testData import validUser, userWithInvalidPassword, userWithInvalidUsername, signInPageUrl



class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(signInPageUrl)

    def test_positive_login(self):
        logInPageObj= LoginPage(self.driver)
        logInPageObj.fill_username_field(validUser.username)
        logInPageObj.click_on_continue_button()
        logInPageObj.fill_password_field(validUser.password)
        logInPageObj.click_on_signin_button()
        time.sleep(10)
        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)


    def test_negative_login_invalid_password(self):
        testValue= False
        message= "There was a problem. Your password is incorrect"
        logInPageObj= LoginPage(self.driver)
        logInPageObj.fill_username_field(validUser.username)
        logInPageObj.click_on_continue_button()
        logInPageObj.fill_password_field(userWithInvalidPassword.password)
        logInPageObj.click_on_signin_button()
        time.sleep(10)
        self.assertFalse(testValue, message)

    def test_negative_login_invalid_email(self):
        testValue= False
        message= "There was a problem. We can not find an account with that email address/mobile number"
        logInPageObj= LoginPage(self.driver)
        logInPageObj.fill_username_field(userWithInvalidUsername.username)
        logInPageObj.click_on_continue_button()
        time.sleep(10)
        self.assertFalse(testValue, message)

    def tearDown(self):
        self.driver.close()

