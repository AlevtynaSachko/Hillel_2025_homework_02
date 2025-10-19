from selenium.webdriver.common.by import By
from .base_page import BasePage

class Header(BasePage):
    # Локатори
    BTN_SIGN_IN = (By.CSS_SELECTOR, 'button[qa="login-link"], a[qa="login-link"], button:has(svg[qa="login"])')
    BTN_SIGN_UP = (By.CSS_SELECTOR, 'button[qa="signup-link"], a[qa="signup-link"], a[href*="signup"], button:has(span:contains("Sign up"))')

    def sign_in_button(self):
        return self.find_clickable(*self.BTN_SIGN_IN)

    def sign_up_button(self):
        # іноді реєстрація відкривається через «Sign In» → «Sign up»
        try:
            return self.find_clickable(*self.BTN_SIGN_UP)
        except:
            return None
