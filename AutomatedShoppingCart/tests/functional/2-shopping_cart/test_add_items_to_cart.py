import time
import pytest
from page_objects.login_page import LoginPage


class TestAddItemsShoppingCard:

    @pytest.mark.shopping_cart
    @pytest.mark.functional
    def test_add_items_to_cart(self, random_shopping_cart_fixture, driver):
        """
               Test case to verify adding random products to the shopping cart.
               Args:
                   random_shopping_cart_fixture: Fixture that provides an instance of the shopping cart.
                   driver: WebDriver instance for browser automation.
               """
        shopping_cart_instance = random_shopping_cart_fixture
        logout_page_instance = LoginPage(driver)

        # Get the items currently in the cart
        cart_items = shopping_cart_instance.get_cart_items()

        # Assertion to check if products were added to the cart
        assert len(cart_items) == 2, "Products were not added to cart."

        # Perform logout after the test
        logout_page_instance.execute_logout()





