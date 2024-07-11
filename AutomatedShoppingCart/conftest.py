import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from page_objects.login_page import LoginPage
from page_objects.shopping_cart_page import ShoppingCartPage


@pytest.fixture(scope="function")
def driver(request):
    """
        Fixture to initialize the WebDriver instance based on command-line input.
        Args:
            request: pytest request object containing test session information.
        Returns:
            WebDriver: The WebDriver instance for browser automation.
        """
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")

    if browser == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")

    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    """
        Adds command-line options for pytest.
        Args:
            parser: pytest parser object for adding command-line options.
        """
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )


@pytest.fixture
def login_fixture(driver):
    """
        Fixture to handle login process for tests.
        Args:
            driver: WebDriver instance for browser automation.
        Returns:
            LoginPage: Instance of LoginPage after successful login.
        """
    login_page_instance = LoginPage(driver)
    login_page_instance.open()
    login_page_instance.maximize_window()
    login_page_instance.execute_login("standard_user", "secret_sauce")
    return login_page_instance


@pytest.fixture
def random_shopping_cart_fixture(driver, login_fixture):
    """
        Fixture to prepare a shopping cart with random products after login.
        Args:
            driver: WebDriver instance for browser automation.
            login_fixture: Fixture for logging into the application.
        Returns:
            ShoppingCartPage: Instance of ShoppingCartPage with random products in the cart.
        """
    shopping_cart_instance = ShoppingCartPage(driver)
    shopping_cart_instance.add_random_product_to_cart(num_products=2)
    shopping_cart_instance.go_to_cart()
    yield shopping_cart_instance

