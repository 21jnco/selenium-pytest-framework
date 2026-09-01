from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement

class DropdownPage(BasePage):
    def open(self, URL: str):
        self.driver.get(URL)

    def get_element(self, locator: tuple):
        return self.find_element(locator)

    def select_dropdown(self, element: WebElement, text: str) -> Select:
        return self.select(element, text)

    def get_dropdown_text(self, dropdown: Select) -> str:
        return self.dropdown_text(dropdown)