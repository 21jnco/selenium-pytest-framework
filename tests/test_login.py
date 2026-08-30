import pytest
from pages.login_page import LoginPage
from selenium.webdriver.chrome.webdriver import WebDriver
from test_data.users import (
    FAILED_USERNAME,
    SUCCESS_USERNAME,
    FAILED_PASSWORD,
    SUCCESS_PASSWORD,
)

class TestLogin():
    @pytest.fixture(autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver

    SUCCESS_MESSAGE = "You logged into a secure area!"
    FAILED_MESSAGE = "Your username is invalid!" 

    def test_success_login(self):
        login_page = LoginPage(self.driver)

        login_page.open()
        login_page.enter_username(SUCCESS_USERNAME)
        login_page.enter_password(SUCCESS_PASSWORD)
        login_page.click_login()
        message = login_page.get_flash_message()

        assert self.SUCCESS_MESSAGE in message

    def test_failed_login(self):
        login_page = LoginPage(self.driver)
        
        login_page.open()
        login_page.enter_username(FAILED_USERNAME)
        login_page.enter_password(FAILED_PASSWORD)
        login_page.click_login()
        message = login_page.get_flash_message()
        
        assert self.FAILED_MESSAGE in message