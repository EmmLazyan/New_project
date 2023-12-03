from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.__clickToCartButtonLocator = (By.ID, "nav-cart-count")
        self.__deleteFirstProductFromCartPageLocator = (By.CLASS_NAME, "submit.delete.96d7827f-3429-4210-9079-9b7323443509")
        self.__deleteButtonFromCartPageLocator = (By.CLASS_NAME, "a-size-small sc-action-delete")
        self.__cartIsEmptyButtonElementLocator = (By.CLASS_NAME, "a-spacing-mini a-spacing-top-base")
        self.__decelectAllItemsFromCartPageLocator = (By.ID, "deselect-all")


    def click_to_cart_button(self):
        clickToCartButtonElement=self._find_element(*self.__clickToCartButtonLocator)
        self._click(clickToCartButtonElement)

    def delete_First_product_from_cartpage(self):
        deleteButtonElement= self._find_element(*self.__deleteFirstProductFromCartPageLocator)
        self._click(deleteButtonElement)

    def click_delete_button_from_cartpage(self):
        deleteButtonElement= self._find_element(*self.__deleteButtonFromCartPageLocator)
        self._click(deleteButtonElement)

    def click_delete_all_product_from_cart_page(self):
        cartCountNumberElement = self._find_element(*self.__decelectAllItemsFromCartPageLocator)
        self._click(cartCountNumberElement)

    def validate_emptiness_cart_page(self):
        cartButtonElement = self._find_element(*self.__cartIsEmptyButtonElementlocator)
        self._get_element_text(cartButtonElement)

