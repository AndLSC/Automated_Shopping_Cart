import pytest


class TestUpdateShoppingCard:

    @pytest.mark.shopping_cart
    @pytest.mark.functional
    def test_update_items_in_cart(self, random_shopping_cart_fixture):
        """
                Test case to verify updating item in the shopping cart.
                Args:
                    random_shopping_cart_fixture: Fixture that provides an instance of the shopping cart.
                """
        shopping_cart_instance = random_shopping_cart_fixture

        # Remove all items from the shopping cart
        shopping_cart_instance.remove_all_items()

        #Continuing shopping to add new items to the cart
        shopping_cart_instance.continue_shopping()

        #Add new items to the cart
        shopping_cart_instance.add_random_product_to_cart(num_products=2)

        # Validate new content in the shopping cart
        shopping_cart_instance.go_to_cart()
