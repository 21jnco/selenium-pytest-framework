from pages.base_page import BasePage

class CheckboxPage(BasePage):
    def open(self, URL: str):
        self.driver.get(URL)

    def get_elements(self, locator: tuple):
        return self.find_elements(locator)
