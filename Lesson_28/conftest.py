import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.header import Header
from pages.auth_modal import AuthModal
from data.users import make_user

QAUTO_HOST = "qauto2.forstudy.space"
BASIC_USER = os.getenv("QAUTO_USER", "guest")
BASIC_PASS = os.getenv("QAUTO_PASS", "welcome2qauto")


@pytest.fixture(scope="session")
def base_url():
    # Доступ через basic-auth у URL
    return f"https://{BASIC_USER}:{BASIC_PASS}@{QAUTO_HOST}"


@pytest.fixture(scope="session")
def user_data():
    # Унікальні дані користувача
    return make_user()


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1440,900")
    # chrome_options.add_argument("--headless=new")  # увімкни для CI
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=chrome_options)
    yield drv
    drv.quit()


# PageObjects як фікстури (тільки пошук елементів)

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def header(driver):
    return Header(driver)

@pytest.fixture
def auth_modal(driver):
    return AuthModal(driver)


# Фікстури-взаємодії

@pytest.fixture
def open_home(driver, base_url):
    driver.get(base_url)
    # підстраховка на випадок редиректів
    if driver.current_url.rstrip("/") != f"{base_url}":
        driver.get(base_url)

@pytest.fixture
def open_signup_modal(open_home, home_page, auth_modal):
    # відкриваємо модалку реєстрації (без артефактів/логів)
    home_page.open_signup_button().click()

@pytest.fixture
def register_user(open_signup_modal, auth_modal, user_data):
    auth_modal.name_input().send_keys(user_data.name)
    auth_modal.last_name_input().send_keys(user_data.last_name)
    auth_modal.email_input().send_keys(user_data.email)
    auth_modal.password_input().send_keys(user_data.password)
    auth_modal.repeat_password_input().send_keys(user_data.password)
    auth_modal.submit_button().click()
    return user_data

@pytest.fixture
def assert_registration_success(auth_modal):
    def _assert():
        hdr = auth_modal.garage_header()
        text = (hdr.text or "").strip().lower()
        assert any(k in text for k in ["garage", "my garage", "гараж"]), \
            f"Не схоже на дашборд після реєстрації. Заголовок: {text!r}"
    return _assert

@pytest.fixture
def register_and_verify(register_user, assert_registration_success):
    # Фікстура щоб зареєструвати і перевірити результат
    assert_registration_success()
