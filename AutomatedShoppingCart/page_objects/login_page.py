from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage(BasePage):
    __url = "https://www.saucedemo.com/"
    __username_locator = (By.ID, "user-name")
    __password_locator = (By.ID, "password")
    __submit_button = (By.ID, "login-button")
    __error_message_type1 = (By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']")
    __error_message_type2 = (By.XPATH, "//h3[text()='Epic sadface: Password is required']")
    __error_message_type3 = (By.XPATH, "//h3[text()='Epic sadface: Username is required']")
    __logout_menu_locator = (By.ID, "react-burger-menu-btn")
    __logout_locator = (By.LINK_TEXT, "Logout")

    def __init__(self, driver: WebDriver):
        """
                Initializes the LoginPage with a WebDriver instance.
                Args:
                    driver (WebDriver): The WebDriver instance used for browser automation.
                """
        super().__init__(driver)

    def open(self):
        """
                Opens the login page by navigating to the specified URL.
                """
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        """
                Enters the username and password, then submits the login form.
                Args:
                    username (str): The username to enter in the login form.
                    password (str): The password to enter in the login form.
                """
        super()._type(self.__username_locator, username)
        super()._type(self.__password_locator, password)
        super()._click(self.__submit_button)

    def execute_logout(self):
        """
                Executes the logout process by clicking on logout menu and logout button.
                """
        super()._click(self.__logout_menu_locator)
        super()._click(self.__logout_locator)

    def get_error_message(self, message_type='error_type1'):
        """
                Retrieves the error message displayed on the login page.
                Args:
                   message_type (str, optional): The type of error message to retrieve. 
                                      Options are 'error_type1', 'error_type2', 'error_type3'. 
                                      Defaults to 'error_type1'.
                Returns:
                    str: The text of the error message.
                Raises:
                    ValueError: If an unknown message type is provided.
                """
        if message_type == 'error_type1':
            locator = self.__error_message_type1
        elif message_type == 'error_type2':
            locator = self.__error_message_type2
        elif message_type == 'error_type3':
            locator = self.__error_message_type3
        else:  #exception
            raise ValueError(f"Unknown message type: {message_type}")
        return self._get_text(locator, time=3)
