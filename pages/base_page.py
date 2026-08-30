from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)

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