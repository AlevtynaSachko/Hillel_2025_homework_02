import os
import pytest
from novaposhta_tracking_page import NovaPoshtaTrackingPage


@pytest.mark.parametrize(
    "ttn,expected_status",
    [
        ("59001461604101", "Отримана"),
    ],
)

def test_tracking_status_matches_expected(driver, ttn, expected_status):
    page = NovaPoshtaTrackingPage(driver)
    page.open()
    page.accept_cookies_if_visible()
    page.enter_tracking_number_and_submit(ttn)
    page.wait_for_status_block()
    actual = page.get_current_status_text()

    assert actual == expected_status, f"Очікували: {expected_status!r}, отримали: {actual!r}"
    print(f"Статус: {actual}")
