import os
import sys
import time
import logging
import pytest

# Додати шлях до SRC
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../SRC')))

from homework_10 import log_event

LOG_FILE = 'login_system.log'

@pytest.fixture(autouse=True)
def cleanup_log_file():
    logging.shutdown()
    time.sleep(0.1)

    if os.path.exists(LOG_FILE):
        try:
            os.remove(LOG_FILE)
        except PermissionError:
            time.sleep(0.2)
            os.remove(LOG_FILE)

    yield

    logging.shutdown()
    time.sleep(0.1)

    if os.path.exists(LOG_FILE):
        try:
            os.remove(LOG_FILE)
        except PermissionError:
            time.sleep(0.2)
            os.remove(LOG_FILE)

def read_log():
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        return f.read()

def test_log_success_event():
    log_event("lesia", "success")
    content = read_log()
    assert "INFO" in content
    assert "lesia" in content
    assert "success" in content

def test_log_expired_event():
    log_event("olena", "expired")
    content = read_log()
    assert "WARNING" in content
    assert "olena" in content
    assert "expired" in content

def test_log_failed_event():
    log_event("nastysja", "failed")
    content = read_log()
    assert "ERROR" in content
    assert "nastysja" in content
    assert "failed" in content

def test_log_unknown_event_is_error():
    log_event("roksolana", "unknown_status")
    content = read_log()
    assert "ERROR" in content
    assert "roksolana" in content
    assert "unknown_status" in content
