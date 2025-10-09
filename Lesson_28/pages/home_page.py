from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    # Кнопка на hero, що відкриває модалку Registration
    BTN_OPEN_SIGNUP = (
        By.XPATH,
        "//button[contains(@class,'btn') and normalize-space()='Sign up']"
    )

    def open_signup_button(self):
        return self.find_clickable(*self.BTN_OPEN_SIGNUP)
