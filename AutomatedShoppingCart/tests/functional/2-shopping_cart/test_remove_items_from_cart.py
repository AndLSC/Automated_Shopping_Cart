import time

import pytest


class TestRemoveShoppingCard:

    @pytest.mark.shopping_cart
    @pytest.mark.functional
    def test_remove_items_from_cart(self, random_shopping_cart_fixture):
        """
                Test case to verify removing items from the shopping cart.
                Args:
                    random_shopping_cart_fixture: Fixture that provides an instance of the shopping cart.
                """
        shopping_cart_instance = random_shopping_cart_fixture

        # Remove all items from the shopping cart
        shopping_cart_instance.remove_all_items()

        # Validate the shopping cart is empty
        assert shopping_cart_instance.is_cart_empty(), "The shopping cart is not empty removing all items."
