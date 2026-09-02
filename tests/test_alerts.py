import pytest
from pages.alerts_pages import AlertsPage


class TestAlerts():
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = AlertsPage(driver)
        self.page.open()

    TEXT_JS_RESULT = "You successfully clicked an alert"
    TEXT_CONFIRM_RESULT = "You clicked: Ok"
    TEXT_CANCEL_RESULT = "You clicked: Cancel"
    TEXT_PROMPT_RESULT = "You entered: jnco"
    SEND_MESSAGE = "jnco"

    TEXT_JS_ALERT = "I am a JS Alert"
    TEXT_JS_CONFIRM = "I am a JS Confirm"
    TEXT_JS_PROMPT = "I am a JS prompt"

    def test_js_alert(self):
        self.page.click_js_alert()
        alert = self.page.get_alert()

        alert.accept()

        result_text = self.page.get_result_text()

        assert self.TEXT_JS_RESULT in result_text

    def test_confirm_alert(self):
        self.page.click_js_confirm()
        alert = self.page.get_alert()

        alert.accept()

        result_text = self.page.get_result_text()

        assert self.TEXT_CONFIRM_RESULT in result_text

    def test_cancel_alert(self):
        self.page.click_js_confirm()
        alert = self.page.get_alert()

        alert.dismiss()

        result_text = self.page.get_result_text()

        assert self.TEXT_CANCEL_RESULT in result_text

    def test_js_prompt(self):
        self.page.click_js_prompt()
        alert = self.page.get_alert()

        alert.send_keys(self.SEND_MESSAGE)
        alert.accept()
        result_text = self.page.get_result_text()

        assert self.TEXT_PROMPT_RESULT in result_text

    def test_alert_js_text(self):
        self.page.click_js_alert()
        alert = self.page.get_alert()

        text = alert.text

        assert self.TEXT_JS_ALERT in text

    def test_alert_js_confirm(self):
        self.page.click_js_confirm()
        alert = self.page.get_alert()

        text = alert.text

        assert self.TEXT_JS_CONFIRM in text

    def test_alert_js_prompt(self):
        self.page.click_js_prompt()
        alert = self.page.get_alert()

        text = alert.text

        assert self.TEXT_JS_PROMPT in text
        