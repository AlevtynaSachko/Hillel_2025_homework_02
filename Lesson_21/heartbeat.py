from datetime import datetime, timedelta
import re
from pathlib import Path
import logging

INFILE = Path("hblog.txt")
OUTFILE = Path("hb_test.log")

KEY = "TSTFEED0300|7E3E|0400"

# Шукати час після слова Timestamp
TS_RE = re.compile(r"[Tt]imestamp\s*[:=]?\s*([0-2]\d:[0-5]\d:[0-5]\d)")

# пороги
OK_MAX = 31
WARN_MIN, WARN_MAX = 31, 33
ERR_MIN = 33

# налаштовуємо логер
logging.basicConfig(
    filename=OUTFILE,
    filemode="w",
    format="%(levelname)s %(asctime)s heartbeat_gap=%(message)s",
    datefmt="%H:%M:%S",
    level=logging.WARNING  # писати тільки WARNING і ERROR
)
logger = logging.getLogger(__name__)


def extract_ts(line: str):
    m = TS_RE.search(line)
    return datetime.strptime(m.group(1), "%H:%M:%S") if m else None


def analyze_heartbeat(infile=INFILE, key=KEY):
    infile = Path(infile)
    if not infile.exists():
        raise FileNotFoundError(f"Вхідний файл не знайдено: {infile.resolve()}")

    # фільтруємо тільки потрібний key
    filtered = []
    with infile.open("r", encoding="utf-8", errors="ignore") as f:
        for lineno, line in enumerate(f, 1):
            if key in line:
                ts = extract_ts(line)
                if ts:
                    filtered.append((lineno, ts))

    if len(filtered) < 2:
        return  # нема що порівнювати

    # враховувати перехід через північ
    normalized = []
    day_offset = 0
    prev_dt = None
    for lineno, ts in filtered:
        dt = ts + timedelta(days=day_offset)
        if prev_dt and dt < prev_dt:
            day_offset += 1
            dt = ts + timedelta(days=day_offset)
        normalized.append((lineno, dt))
        prev_dt = dt

    # порівняти сусідні записи
    for (ln1, t1), (ln2, t2) in zip(normalized, normalized[1:]):
        secs = int((t2 - t1).total_seconds())

        if WARN_MIN < secs < WARN_MAX:
            logger.warning(f"{secs}s (lines {ln1}->{ln2}) key={key}")
        elif secs >= ERR_MIN:
            logger.error(f"{secs}s (lines {ln1}->{ln2}) key={key}")
        # нормальні (≤31) не пишемо


if __name__ == "__main__":
    analyze_heartbeat()
    print(f"Готово. Подивись файл: {OUTFILE}")

