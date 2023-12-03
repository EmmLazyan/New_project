import time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from tests_.baseTest import baseTestWithLogin
from pages_.cartPage import CartPage

class cart(baseTestWithLogin):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())


    def test_cart_page_emptiness(self):
        value = True
        massege = "Warning. The cart is empty"
        cartPageObj= CartPage(self.driver)
        cartPageObj.click_to_cart_button()
        time.sleep(10)

        self.assertTrue(value, massege)


    def test_delete_first_product_from_cart_page(self):
        cartPageObj = CartPage(self.driver)
        cartPageObj.click_to_cart_button()
        cartPageObj.click_delete_button_from_cartpage()
        time.sleep(10)

    def test_delete_all_product_from_cart_page(self):
        cartPageObj = CartPage(self.driver)
        cartPageObj.click_to_cart_button()
        cartPageObj.click_delete_all_product_from_cart_page()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()