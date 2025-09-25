import os
import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

LOG_FILE = "test_search.log"
LOGGER_NAME = "cars_api_tests"

def _build_logger() -> logging.Logger:
    logger = logging.getLogger(LOGGER_NAME)
    if logger.handlers:
        return logger  # вже налаштовано (уникаємо дублю хендлерів)

    logger.setLevel(logging.INFO)

    fmt = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Консоль
    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    # Файл
    fh = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    logger.info("Логування ініціалізовано. Пишемо у консоль і файл %s", LOG_FILE)
    return logger

@pytest.fixture(scope="session")
def logger():
    """Сесійний логер, доступний у всіх тестах."""
    return _build_logger()

@pytest.fixture(scope="class")
def api_session(request, logger):
    """
    Класова фікстура: виконує початкову аутентифікацію і повертає готову Session
    з прописаним Bearer-токеном в headers.
    """
    base_url = os.getenv("CARS_API_BASE_URL", "http://127.0.0.1:8080")
    username = os.getenv("CARS_API_USER", "test_user")
    password = os.getenv("CARS_API_PASS", "test_pass")

    s = requests.Session()
    auth = HTTPBasicAuth(username, password)
    auth_url = f"{base_url}/auth"

    logger.info("Аутентифікація: POST %s як %s", auth_url, username)
    resp = s.post(auth_url, auth=auth)
    logger.info("Відповідь /auth: %s | body: %s", resp.status_code, resp.text)

    resp.raise_for_status()
    token = resp.json()["access_token"]
    s.headers.update({"Authorization": f"Bearer {token}"})

    # прокинути в клас
    request.cls.base_url = base_url
    request.cls.session = s
    request.cls.logger = logger

    return s
