def logger(func):
    def wrapper(*args, **kwargs):
        log_text = f"Виклик функції {func.__name__} з аргументами: {args}, {kwargs}\n"
        result = func(*args, **kwargs)
        log_text += f"Результат: {result}\n"
        print(log_text)

        # Додати у файл log.txt
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(log_text)

        return result
    return wrapper


@logger
def add(a, b):
    return a + b

# наприклад
add(a=50, b=70)
add(a=65, b=75)
add(a=122, b=144)
