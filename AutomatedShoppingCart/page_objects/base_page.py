from typing import List
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        """
                Initializes the BasePage with a WebDriver instance.
                Args:
                    driver (WebDriver): The WebDriver instance used for browser automation.
                """
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        """
               Finds a single web element based on the locator.
               Args:
                   locator (tuple): A tuple containing the locator strategy and value.
               Returns:
                   WebElement: The WebElement object found.
               """
        return self._driver.find_element(*locator)

    def _find_all(self, locator: tuple[str, str]) -> List[WebElement]:
        """
                Finds all web elements matching the locator.
                Args:
                    locator (tuple[str, str]): A tuple containing the locator strategy and value.
                Returns:
                    List[WebElement]: A list of WebElement objects found.
                """
        return self._driver.find_elements(*locator)

    def _click(self, locator: tuple, time: int = 10):
        """
                Waits for an element to be visible and then clicks it.
                Args:
                    locator (tuple): A tuple containing the locator strategy and value.
                    time (int, optional): Maximum time to wait for the element to be visible. Defaults to 10 seconds.
                """
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _type(self, locator: tuple, text: str, time: int = 10):
        """
                Waits for an element to be visible and then types text into it.
                Args:
                    locator (tuple): A tuple containing the locator strategy and value.
                    text (str): The text to type into the element.
                    time (int, optional): Maximum time to wait for the element to be visible. Defaults to 10 seconds.
                """
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _open_url(self, url: str):
        """
                Opens a URL in the browser.
                Args:
                    url (str): The URL to open.
                """
        self._driver.get(url)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        """
                Waits until an element is visible on the page.
                Args:
                    locator (tuple): A tuple containing the locator strategy and value.
                    time (int, optional): Maximum time to wait for the element to be visible. Defaults to 10 seconds.
                """
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _get_text(self, locator, time: int = 3):
        """
                Waits until an element is present on the page and retrieves its text.
                Args:
                    locator (tuple): A tuple containing the locator strategy and value.
                    time (int, optional): Maximum time to wait for the element to be present. Defaults to 3 seconds.
                Returns:
                    str: The text of the element if found, otherwise returns "Element not found".
                """
        try:
            element = WebDriverWait(self._driver, time).until(
                ec.presence_of_element_located(locator)
            )
            return element.text
        except TimeoutException:
            return "Element not found"

    def maximize_window(self):
        """
               Maximizes the browser window.
               """
        self._driver.maximize_window()

    def close(self):
        """
                Closes the browser.
                """
        self._driver.quit()

    @property
    def current_url(self) -> str:
        """
                Returns the current URL of the browser.
                Returns:
                    str: The current URL.
                """
        return self._driver.current_url

    def come_back(self):
        """
                Navigates back to the previous page in the browser history.
                """
        self._driver.back()

