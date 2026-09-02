from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    def open(self):
        self.driver.get(self.URL)
        
    def loaging_click(self, locator: tuple):
        self.click(locator)

    def get_hello_world_text(self, locator):
        return self.get_text(locator)




