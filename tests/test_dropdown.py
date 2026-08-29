import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from locators.dropdown_locators import DROPDOWN_BUTTON


class TestDropdown():
    @pytest.fixture(autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver

    URL = "https://the-internet.herokuapp.com/dropdown"
    OPTION = "Option 2"

    def test_dropdown(self):
        self.driver.get(self.URL)
        element = self.driver.find_element(DROPDOWN_BUTTON)
        dropdown = Select(element)
        dropdown.select_by_value("2")
        selected_text = dropdown.first_selected_option.text

        assert self.OPTION in selected_text
        