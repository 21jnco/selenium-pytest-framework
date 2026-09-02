from pages.base_page import BasePage
from selenium.webdriver.common.alert import Alert
from locators.alerts_locators import JS_ALERT, JS_PROMPT, JS_CONFIRM, RESULT


class AlertsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def open(self):
        self.driver.get(self.URL)

    def click_js_alert(self):
        self.click(JS_ALERT)

    def click_js_prompt(self):
        self.click(JS_PROMPT)

    def click_js_confirm(self):
        self.click(JS_CONFIRM)

    def get_alert(self):
        return self.alert_is_present()

    def get_result_text(self):
        return self.get_text(RESULT)
