from pages.base_page import BasePage

class CheckboxPage(BasePage):
    URL = "https://the-internet.herokuapp.com/checkboxes"

    def open(self):
        self.driver.get(self.URL)

    def get_elements(self, locator: tuple):
        return self.find_elements(locator)
