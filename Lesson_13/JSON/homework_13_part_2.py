import json
import logging
from pathlib import Path

# Налаштування логера
log_file = Path(__file__).parent / "json_Sachko.log"

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler() # вивід у консоль
    ]
)

# Шлях
json_dir = Path(__file__).parent / "JSON"

# Проходимо по кожному файлу
for json_file in json_dir.glob("*.json"):
    try:
        with open(json_file, encoding="utf-8") as f:
            json.load(f)
        print(f"✅ {json_file.name} — валідний")
    except json.JSONDecodeError as e:
        logging.error(f"{json_file.name} — помилка: {e}")
    except Exception as e:
        logging.error(f"{json_file.name} — інша помилка: {e}")