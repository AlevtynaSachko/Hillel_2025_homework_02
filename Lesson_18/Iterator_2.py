class EvenIterator:
    def __init__(self, n):
        self.n = n # межа (останнє число, яке можна вивести)
        self.current = 0 # починаємо з нуля

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n: # якщо вже більші за N → зупиняємось
            raise StopIteration
        value = self.current # зберігаємо поточне значення
        self.current += 2 # робимо крок одразу на наступне парне
        return value


# наприклад
for x in EvenIterator(44):
    print(x, end=" ")