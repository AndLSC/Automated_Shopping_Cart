import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CheckoutPage(BasePage):
    __checkout_button_locator = (By.ID, "checkout")
    __first_name_locator = (By.ID, "first-name")
    __last_name_locator = (By.ID, "last-name")
    __postal_code_locator = (By.ID, "postal-code")
    __continue_button_locator = (By.ID, "continue")
    __finish_button_locator = (By.ID, "finish")
    __home_button_locator = (By.ID, "back-to-products")
    __header_locator = (By.TAG_NAME, "h2")

    def __init__(self, driver: WebDriver):
        """
                Initializes the CheckoutPage with a WebDriver instance.
                Args:
                    driver (WebDriver): The WebDriver instance used for browser automation.
                """
        super().__init__(driver)

    def checkout_products(self):
        """
                Clicks on the checkout button to proceed with checkout.
                """
        super()._click(self.__checkout_button_locator)

    def checkout_information(self, first_name: str, last_name: str, postal_code: str):
        """
                Enters checkout information and completes the checkout process.
                Args:
                    first_name (str): The first name to enter in the checkout form.
                    last_name (str): The last name to enter in the checkout form.
                    postal_code (str): The postal code to enter in the checkout form.
                """
        super()._type(self.__first_name_locator, first_name)
        super()._type(self.__last_name_locator, last_name)
        super()._type(self.__postal_code_locator, postal_code)
        super()._click(self.__continue_button_locator)
        super()._click(self.__finish_button_locator)
        
    @property
    def header(self):
        """
                Returns the text of the header element on the checkout page.
                Returns:
                    str: The text of the header element.
                """
        return self._get_text(self.__header_locator)

    def come_back(self):
        """
                Navigates back to the home page.
                """
        return self._click(self.__home_button_locator)
