import random
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ShoppingCartPage(BasePage):
    __cart_locator = (By.ID, "shopping_cart_container")
    __continue_shopping_locator = (By.ID, "continue-shopping")
    __cart_item_locator = (By.CLASS_NAME, "inventory_item_name")
    __inventory_item_locator = (By.CLASS_NAME, "inventory_item")
    __remove_button_locator = (By.XPATH, "//button[contains(text(), 'Remove')]")
    __add_to_cart_button_locator_template = "//button[contains(@id, 'add-to-cart-{}')]"

    def __init__(self, driver: WebDriver):
        """
                Initializes the ShoppingCartPage with a WebDriver instance.
                Args:
                    driver (WebDriver): The WebDriver instance used for browser automation.
                """
        super().__init__(driver)

    def go_to_cart(self):
        """
               Navigates to the shopping cart page by clicking on the cart icon.
               """
        super()._wait_until_element_is_visible(self.__cart_locator, time=10)
        super()._click(self.__cart_locator)

    def continue_shopping(self):
        """
                Clicks on the 'Continue Shopping' button to return to the main shopping page.
                """
        super()._click(self.__continue_shopping_locator)

    def get_cart_items(self):
        """
                Retrieves the names of all items in the shopping cart.
                Returns:
                    list: A list containing the names of all items in the shopping cart.
                """
        elements = self._driver.find_elements(*self.__cart_item_locator)
        return [element.text for element in elements]

    def is_cart_empty(self):
        """
                Checking if the shopping cart is empty.
                Returns:
                list: A list containing the names of all items in the shopping cart, it must empty.
                """
        return len(self.get_cart_items()) == 0

    def add_product_to_cart(self, product_name: str):
        product_name_formatted = product_name.lower().replace(" ", "-")
        add_to_cart_button_locator = (By.XPATH, self.__add_to_cart_button_locator_template.format(product_name_formatted))
        super()._click(add_to_cart_button_locator)

    def add_random_product_to_cart(self, num_products):
        """
                Adds a specified number of random products to the shopping cart.
                Args:
                    num_products (int): The number of random products to add to the cart.
                """
        for _ in range(num_products):
            inventory_items = self._find_all(self.__inventory_item_locator)
            random_product = random.choice(inventory_items)
            random_product_name = random_product.find_element(By.CLASS_NAME,
                                                              "inventory_item_name").text.lower().replace(" ", "-")
            self.add_product_to_cart(random_product_name)

    def remove_all_items(self):
        """
                Removes all items from the shopping cart.
                """
        try:
            remove_buttons = self._find_all(self.__remove_button_locator)
            for button in remove_buttons:
                button.click()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Could not remove all items due to: {type(e).__name__}")
