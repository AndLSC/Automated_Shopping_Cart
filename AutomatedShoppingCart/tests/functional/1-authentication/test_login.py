import time

import pytest

from page_objects.login_page import LoginPage


class TestLogin:

    @pytest.mark.login
    @pytest.mark.authentication
    def test_login(self, login_fixture):
        """
                Test successful login with valid credentials.
                Args:
                    login_fixture: Fixture that logs in with standard_user and secret_sauce.
                Asserts:
                    Verifies that after login, the current URL is correct.
                """
        login_page_instance = login_fixture
        assert login_page_instance.current_url == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.login
    @pytest.mark.authentication
    @pytest.mark.parametrize("username, password, expected_error_message, message_type",
                             [("incorrectUser", "secret_sauce",
                               "Epic sadface: Username and password do not match any user in this service", "error_type1"),
                              ("standard_user", "incorrectPassword",
                               "Epic sadface: Username and password do not match any user in this service", "error_type1"),
                              ("standard_user", "", "Epic sadface: Password is required", "error_type2"),
                              ("", "secret_sauce", "Epic sadface: Username is required", "error_type3"),
                              ("", "", "Epic sadface: Username is required", "error_type3")])
    def test_login_failed(self, driver, username, password, expected_error_message, message_type):
        """
                Test login with invalid credentials.
                Args:
                    driver: WebDriver instance for browser automation.
                    username: Username to attempt login with.
                    password: Password to attempt login with.
                    expected_error_message: Expected error message when login fails.
                    message_type: Type of error message (error_type1, error_type2 or error_type3).
                """
        login_page_instance = LoginPage(driver)

        # Opens the login page.
        login_page_instance.open()

        # Maximizes the browser window.
        login_page_instance.maximize_window()

        # Attempts to login with provided credentials.
        login_page_instance.execute_login(username, password)

        # Asserts that the error message matches the expected error message.
        assert login_page_instance.get_error_message(
            message_type) == expected_error_message, "Error message is not expected"
