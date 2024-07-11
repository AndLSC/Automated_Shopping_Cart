import pytest


class TestLogout:

    @pytest.mark.logout
    @pytest.mark.authentication
    def test_logout(self, driver, login_fixture):
        """
               Test successful logout after login.
               Args:
                   driver: WebDriver instance for browser automation.
                   login_fixture: Fixture that logs in with standard_user and secret_sauce.
               Asserts:
                   Verifies that after logout, the current URL is correct.
               """
        login_page_instance = login_fixture
        login_page_instance.execute_logout()
        assert driver.current_url == "https://www.saucedemo.com/"

