import time
import pytest
from page_objects.checkout_page import CheckoutPage
from page_objects.login_page import LoginPage


class TestCheckoutProcess:

    @pytest.mark.checkout
    @pytest.mark.functional
    def test_checkout_process(self, driver, random_shopping_cart_fixture):
        """
                Test the checkout process with a random shopping cart.
                Args:
                    driver: WebDriver instance for browser automation.
                    random_shopping_cart_fixture: Fixture for a shopping cart with random products.
                    """
        # Instances
        logout_page_instance = LoginPage(driver)
        checkout_instance = CheckoutPage(driver)
        
        # Perform checkout process
        checkout_instance.checkout_products()
        time.sleep(4)
        # Provide checkout information
        checkout_instance.checkout_information("Maria", "Perez", "VG8TA6")
        time.sleep(4)
        # Verify checkout order is completed
        assert checkout_instance.header == "Thank you for your order!", "Header is not expected"
        
        # Return to previous page after checkout
        checkout_instance.come_back()
        
        # Logout after completing the checkout process
        logout_page_instance.execute_logout()
