class Rhombus:
    def __init__(self, storona_a, kut_a):
        self.storona_a = storona_a
        self.kut_a = kut_a
        self.kut_b = 180 - kut_a

    def __setattr__(self, key, value):
        if key == "storona_a":
            if value <= 0:
                raise ValueError
        elif key == "kut_a":
            if not (0 < value < 180):
                raise ValueError
            super().__setattr__("kut_b", 180 - value)

        super().__setattr__(key, value)

    def __repr__(self):
        return f"Rhombus(storona_a={self.storona_a}, kut_a={self.kut_a}, kut_b={self.kut_b})"


#Приклад
r = Rhombus(10, 60)
print(r) # очікуємо що Rhombus(storona_a=10, kut_a=60, kut_b=120)

r.kut_a = 75
print(r) # очікуємо що Rhombus(storona_a=10, kut_a=75, kut_b=105)

try: #використовуємо try там де хочемо перевірити помилку
    r.storona_a = -5
except ValueError as e:
    print("Помилка: застосоване некоректне значення", e)