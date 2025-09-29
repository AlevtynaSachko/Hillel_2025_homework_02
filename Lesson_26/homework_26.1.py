from pathlib import Path
import subprocess, socket, time, sys
from contextlib import closing

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def wait_port(host: str, port: int, timeout: float = 5.0) -> None:
    """Очікуємо, поки порт стане доступним."""
    start = time.time()
    while time.time() - start < timeout:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(0.5)
            if sock.connect_ex((host, port)) == 0:
                return
        time.sleep(0.1)
    raise RuntimeError(f"Порт {port} недоступний (сервер не стартував).")


def run_test(base_url: str) -> None:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(base_url + "/dz.html")

        # ===== Frame 1 =====
        driver.switch_to.frame("frame1")
        wait.until(EC.presence_of_element_located((By.ID, "input1"))).send_keys("Frame1_Secret")
        driver.find_element(By.TAG_NAME, "button").click()
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert alert.text == "Верифікація пройшла успішно!"
        print("[OK] Frame1:", alert.text)
        alert.accept()
        driver.switch_to.default_content()

        # ===== Frame 2 =====
        driver.switch_to.frame("frame2")
        wait.until(EC.presence_of_element_located((By.ID, "input2"))).send_keys("Frame2_Secret")
        driver.find_element(By.TAG_NAME, "button").click()
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert alert.text == "Верифікація пройшла успішно!"
        print("[OK] Frame2:", alert.text)
        alert.accept()
        driver.switch_to.default_content()

        print("\n✅ Завдання виконано успішно.")
    finally:
        driver.quit()


if __name__ == "__main__":
    # Папка з HTML
    webroot = Path(__file__).resolve().parent

    # 1) підіймаємо локальний сервер на 8000 порті саме з цієї папки
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", "8000"],
        cwd=str(webroot),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        wait_port("127.0.0.1", 8000, timeout=5.0)
        run_test("http://127.0.0.1:8000")
    finally:
        server.terminate()
        try:
            server.wait(timeout=2)
        except subprocess.TimeoutExpired:
            server.kill()
