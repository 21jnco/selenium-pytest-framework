import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from locators.checkbox_locators import CHECKBOX_ELEMENT
from pages.checkbox_page import CheckboxPage


class TestCheckbox():
    @pytest.fixture(autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver

    def test_checkboxes(self):
        checkbox_page = CheckboxPage(self.driver)

        checkbox_page.open()
        checkboxes = checkbox_page.find_elements(CHECKBOX_ELEMENT)
        assert checkboxes[0].is_selected() is False
        assert checkboxes[1].is_selected() is True

        checkboxes[0].click()

        assert checkboxes[0].is_selected() is True