from selenium.webdriver.common.by import By


USERNAME_INPUT = (By.ID, "username")
PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
FLASH_MESSAGE = (By.ID, "flash")