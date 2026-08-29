import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from locators.checkbox_locators import CHECKBOX_ELEMENT


class TestCheckbox():
    @pytest.fixture(autouse=True)
    def setup(self, driver: WebDriver):
        self.driver = driver

    URL = "https://the-internet.herokuapp.com/checkboxes"

    def test_checkboxes(self):
        self.driver.get(self.URL)
        checkboxes = self.driver.find_elements(
            By.CSS_SELECTOR,
            CHECKBOX_ELEMENT
        )

        assert checkboxes[0].is_selected() is False
        assert checkboxes[1].is_selected() is True

        checkboxes[0].click()
        checkbox = self.driver.find_element(
            By.CSS_SELECTOR,
            CHECKBOX_ELEMENT
        )

        assert checkbox.is_selected() is True