import logging
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(), # для консолі
        logging.FileHandler("log.txt", encoding="utf-8") # писати в файл
    ]
)

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Виклик функції {func.__name__} з аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Результат: {result}")
        return result
    return wrapper


@logger
def add(a, b):
    return a + b


#наприклад
add(a=50, b=70)
add(a=65, b=75)
add(a=122, b=144)