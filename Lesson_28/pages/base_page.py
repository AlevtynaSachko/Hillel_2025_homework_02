from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 20

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def find_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def wait_visible(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))



