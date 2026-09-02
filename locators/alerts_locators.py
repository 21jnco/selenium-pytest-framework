from selenium.webdriver.common.by import By

JS_ALERT = (By.CSS_SELECTOR, 'button[onclick="jsAlert()"]')
JS_CONFIRM = (By.CSS_SELECTOR, 'button[onclick="jsConfirm()"]')
JS_PROMPT = (By.CSS_SELECTOR, 'button[onclick="jsPrompt()"]')
RESULT = (By.ID, "result")