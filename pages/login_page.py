import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.login_locators import(
    USERNAME_INPUT,
    LOGIN_BUTTON,
    PASSWORD_INPUT,
    FLASH_MESSAGE
)
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, USERNAME: str):
        self.type_text(USERNAME_INPUT, USERNAME)

    def enter_password(self, PASSWORD: str):
        self.type_text(PASSWORD_INPUT, PASSWORD)

    def click_login(self):
        self.click(LOGIN_BUTTON)

    def get_flash_message(self):
        return self.get_text(FLASH_MESSAGE)