import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.dropdown_page import DropdownPage
from locators.dropdown_locators import DROPDOWN_BUTTON
from pages.dropdown_page import DropdownPage

class TestDropdown():
    @pytest.fixture(autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver

    OPTION = "Option 1"

    def test_dropdown(self):
        dropdown_page = DropdownPage(self.driver)

        dropdown_page.open()
        element = dropdown_page.get_element(DROPDOWN_BUTTON)
        dropdown = dropdown_page.select_dropdown(element, self.OPTION)
        text = dropdown_page.get_dropdown_text(dropdown)

        assert self.OPTION in text
        