def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.__name__} з аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper


@logger
def add(a, b):
    return a + b

# наприклад
add(50, 70)