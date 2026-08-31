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

    def enter_username(self, username: str):
        self.type_text(USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.type_text(PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LOGIN_BUTTON)

    def get_flash_message(self):
        return self.get_text(FLASH_MESSAGE)