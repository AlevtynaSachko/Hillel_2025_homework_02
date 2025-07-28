"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.
    status: Статус події входу:
        * success - успішний (рівень INFO)
        * expired - пароль застарів (рівень WARNING)
        * failed  - невірний пароль або інша помилка (рівень ERROR)
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Конфігурація логера з force=True, щоб оновити налаштування навіть якщо вже були задані
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True
    )
    logger = logging.getLogger("log_event")

    # Логування відповідно до статусу
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
