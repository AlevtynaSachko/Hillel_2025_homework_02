from selenium.webdriver.common.by import By
from .base_page import BasePage

class AuthModal(BasePage):
    # Поля реєстрації
    INP_NAME = (By.ID, "signupName")
    INP_LASTNAME = (By.ID, "signupLastName")
    INP_EMAIL = (By.ID, "signupEmail")
    INP_PASSWORD = (By.ID, "signupPassword")
    INP_REPEAT = (By.ID, "signupRepeatPassword")
    BTN_SUBMIT = (By.XPATH, "//button[contains(@class,'btn-primary') and text()='Register']")

    # Після реєстрації сторінка перекидає у Garage
    GARAGE_HEADER = (By.XPATH, "//h1[contains(text(),'Garage') or contains(text(),'Гараж')]")

    def name_input(self): return self.find(*self.INP_NAME)
    def last_name_input(self): return self.find(*self.INP_LASTNAME)
    def email_input(self): return self.find(*self.INP_EMAIL)
    def password_input(self): return self.find(*self.INP_PASSWORD)
    def repeat_password_input(self): return self.find(*self.INP_REPEAT)
    def submit_button(self): return self.find_clickable(*self.BTN_SUBMIT)
    def garage_header(self): return self.wait_visible(*self.GARAGE_HEADER)
