def error_catcher(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виникла помилка у {func.__name__}: {e}")
            return None

    return wrapper


@error_catcher
def divide(a, b):
    return a / b


# наприклад
print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Виникла помилка у divide: division by zero


