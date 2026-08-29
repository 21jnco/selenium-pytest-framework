import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from test_data.users import (
    FAILED_USERNAME,
    SUCCESS_USERNAME,
    FAILED_PASSWORD,
    SUCCESS_PASSWORD
)
from locators.login_locators import(
    USERNAME_INPUT,
    LOGIN_BUTTON,
    PASSWORD_INPUT,
    FLASH_MESSAGE
)

class TestLogin():
    @pytest.fixture(autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver

    URL = "https://the-internet.herokuapp.com/login"
    SUCCESS_MESSAGE = "You logged into a secure area!"
    FAILED_MESSAGE = "Your username is invalid!"

    def test_success_login(self):
        self.driver.get(self.URL)
        element_username = self.driver.find_element(*USERNAME_INPUT)
        element_password = self.driver.find_element(*PASSWORD_INPUT)
        element_button = self.driver.find_element(*LOGIN_BUTTON)

        element_username.send_keys(SUCCESS_USERNAME)
        element_password.send_keys(SUCCESS_PASSWORD)
        element_button.click()

        message = self.driver.find_element(*FLASH_MESSAGE).text

        assert self.SUCCESS_MESSAGE in message

    def test_failed_login(self):
        self.driver.get(self.URL)
        element_username = self.driver.find_element(*USERNAME_INPUT)
        element_password = self.driver.find_element(*PASSWORD_INPUT)
        element_button = self.driver.find_element(*LOGIN_BUTTON)

        element_username.send_keys(FAILED_USERNAME)
        element_password.send_keys(FAILED_PASSWORD)
        element_button.click()

        message = self.driver.find_element(*FLASH_MESSAGE).text

        assert self.FAILED_MESSAGE in message
