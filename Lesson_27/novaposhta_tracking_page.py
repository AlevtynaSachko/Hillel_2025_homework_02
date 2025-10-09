from dataclasses import dataclass
from typing import Optional
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 25

@dataclass
class NovaPoshtaTrackingPage:
    driver: WebDriver
    base_url: str = "https://tracking.novaposhta.ua/#/uk"
    timeout: int = DEFAULT_TIMEOUT

    # Основні локатори (із запасними варіантами)
    _search_input_locators = (
        # найчастіше — звичайний <input> із placeholder’ом
        (By.CSS_SELECTOR, "input[placeholder*='Введіть'][placeholder*='накладної']"),
        # інколи використовують загальне поле пошуку
        (By.CSS_SELECTOR, "input[type='search']"),
        # запасний варіант через role/aria
        (By.XPATH, "//input[contains(@placeholder,'ТТН') or contains(@aria-label,'ТТН') or contains(@aria-label,'накладної')]"),
        # ще один запасний — перший помітний input у шапці
        (By.XPATH, "(//input)[1]"),
    )

    _status_text_locators = (
        (By.CSS_SELECTOR, ".header__status-text"),
        (By.XPATH, "//div[contains(@class,'header__status-text')]"),
        (By.XPATH, "//div[contains(text(),'Зараз:')]/following::div[contains(@class,'status-text')][1]"),
        (By.XPATH, "//*[contains(text(),'Зараз')]/following::*[1]"),
    )

    _cookie_accept_locators = (
        (By.XPATH, "//button[.//text()[contains(.,'Прийняти')]]"),
        (By.XPATH, "//button[.//text()[contains(.,'Прийняти всі') or contains(.,'Прийняти всі файли cookie')]]"),
        (By.XPATH, "//button[.//text()[contains(.,'Погоджуюсь')] or .//text()[contains(.,'Погодитися')]]"),
    )

    def open(self) -> None:
        self.driver.get(self.base_url)

    def _find_first_visible(self, locators) -> Optional[tuple]:
        for by, sel in locators:
            try:
                el = WebDriverWait(self.driver, 2).until(
                    EC.visibility_of_element_located((by, sel))
                )
                return (by, sel)
            except Exception:
                continue
        return None

    def accept_cookies_if_visible(self) -> None:
        # без падіння: клікаємо першу доступну кнопку з текстом "Прийняти" тощо
        for by, sel in self._cookie_accept_locators:
            try:
                btn = WebDriverWait(self.driver, 1).until(
                    EC.element_to_be_clickable((by, sel))
                )
                btn.click()
                break
            except Exception:
                continue

    def enter_tracking_number_and_submit(self, ttn: str) -> None:
        input_loc = self._find_first_visible(self._search_input_locators)
        if not input_loc:
            raise RuntimeError("Не знайшов поле вводу для номера накладної. Онови локатори.")

        input_el = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(input_loc)
        )
        # Очистка + введення
        input_el.clear()
        input_el.send_keys(ttn)
        input_el.send_keys(Keys.ENTER)

    def wait_for_status_block(self) -> None:
        # Очікуємо, доки завантажиться блок зі статусом (будь-який з відомих локаторів)
        for by, sel in self._status_text_locators:
            try:
                WebDriverWait(self.driver, self.timeout).until(
                    EC.visibility_of_element_located((by, sel))
                )
                return
            except Exception:
                continue
        raise TimeoutError("Статус не з’явився в інтерфейсі протягом очікування.")

    def get_current_status_text(self) -> str:
        # Зчитуємо перший, що з’явився, статус
        for by, sel in self._status_text_locators:
            try:
                el = WebDriverWait(self.driver, 1).until(
                    EC.visibility_of_element_located((by, sel))
                )
                text = el.text.strip()
                if text:
                    return text
            except Exception:
                continue
        raise RuntimeError("Не вдалося зчитати текст статусу. Онови локатори.")
