from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.__searchFieldLocator = (By.NAME, "field-keywords")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")
        self.__firstProductLocator = (By.XPATH, "(//span[@class='s-heavy'])[1]")
        self.__addToShoppingCartLocator = (By.ID, "addToCart_feature_div")
        self.__resultPageLocator = (By.XPATH, "(//span[@class='a-size-medium a-color-base a-text-normal'])[15]")


    def click_to_search_Button(self):
        searchButtonElement= self._find_element(*self.__searchButtonLocator)
        self._click(searchButtonElement)

    def click_to_the_first_product(self):
        firstProductElement = self._find_element(*self.__firstProductLocator)
        self._click(firstProductElement)

    def _fill_search_field(self, text):
        searchFieldElement = self._find_element(*self.__searchFieldLocator)
        self._fill_field(searchFieldElement, text)

    def click_to_result_element(self):
        resultPageElement = self._find_element(*self.__resultPageLocator)
        self._click(resultPageElement)

    def click_to_add_button(self):
        addButtonElement = self._find_element(*self.__addToShoppingCartLocator)
        self._click(addButtonElement)