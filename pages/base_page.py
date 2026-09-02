from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement


class BasePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple):
        wait_element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )
        wait_element.click()

    def type_text(self, locator, text: str):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def get_text(self, locator: tuple):
        wait_locator = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        ).text

        return wait_locator

    def select(self, element: WebElement, text: str):
        dropdown = Select(element)
        dropdown.select_by_visible_text(text)

        return dropdown

    def dropdown_text(self, dropdown: Select):
        return dropdown.first_selected_option.text

    def alert_is_present(self):
        return WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )
