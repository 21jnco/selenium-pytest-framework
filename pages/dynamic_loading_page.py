from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    def open(self, URL: str):
        self.driver.get(URL)
        
    def loaging_click(self, locator: tuple):
        self.click(locator)

    def get_hello_world_text(self, locator):
        return self.get_text(locator)




