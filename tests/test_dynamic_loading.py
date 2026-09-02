import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.dynamic_loading_page import DynamicLoadingPage

from locators.dynamic_loading_locators import START_BUTTON, FINISH_LOCATOR

class TestDynamicLoading():
    @pytest.fixture(autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver

    TEXT_HELLO = "Hello World!"

    def test_dynamic_loading(self):
        dynamic_page = DynamicLoadingPage(self.driver)

        dynamic_page.open()
        dynamic_page.loaging_click(START_BUTTON)
        text = dynamic_page.get_hello_world_text(FINISH_LOCATOR)
        
        assert self.TEXT_HELLO in text

        