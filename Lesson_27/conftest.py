import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    headless = os.getenv("HEADLESS", "1") == "1"

    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,900")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--lang=uk")
    options.add_argument("--force-device-scale-factor=1")

    drv = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                           options=options)
    yield drv
    drv.quit()
