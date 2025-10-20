import os
import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth
import allure

LOG_FILE = "test_search.log"
LOGGER_NAME = "cars_api_tests"


def _build_logger() -> logging.Logger:
    """Створює консольний + файловий логер (idempotent)."""
    logger = logging.getLogger(LOGGER_NAME)
    if logger.handlers:
        return logger

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
    Класова фікстура: отримує JWT-токен через /auth і повертає готовий
    requests.Session з Authorization: Bearer <token>.
    Також пробрасыває base_url, session і logger у тест-клас.
    """
    base_url = os.getenv("CARS_API_BASE_URL", "http://127.0.0.1:8080")
    username = os.getenv("CARS_API_USER", "test_user")
    password = os.getenv("CARS_API_PASS", "test_pass")

    s = requests.Session()
    auth_url = f"{base_url}/auth"

    with allure.step("Отримати JWT-токен через /auth"):
        logger.info("Аутентифікація: POST %s як %s", auth_url, username)
        resp = s.post(auth_url, auth=HTTPBasicAuth(username, password))
        logger.info("Відповідь /auth: %s | body: %s", resp.status_code, resp.text)
        # якщо статус не 2xx — хай впаде тут (у степі буде видно помилку)
        resp.raise_for_status()

        token = resp.json()["access_token"]
        s.headers.update({"Authorization": f"Bearer {token}"})

        # Додамо тіло відповіді до репорту
        try:
            allure.attach(resp.text, "auth_response.json", allure.attachment_type.JSON)
        except Exception:
            # якщо з JSON щось піде не так — прикріпити як текст
            allure.attach(resp.text, "auth_response.txt", allure.attachment_type.TEXT)

    # атрибути в тест-класі
    request.cls.base_url = base_url
    request.cls.session = s
    request.cls.logger = logger

    return s


def pytest_sessionfinish(session, exitstatus):
    """
    Після завершення всієї сесії тестів — прикріпити лог-файл у Allure.

    """
    try:
        if os.path.exists(LOG_FILE):
            allure.attach.file(
                LOG_FILE,
                name=LOG_FILE,
                attachment_type=allure.attachment_type.TEXT,
            )
    except Exception:
        # не ламаємо завершення ранeру, якщо attach не вдався
        pass

