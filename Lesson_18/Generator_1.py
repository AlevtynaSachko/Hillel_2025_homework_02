def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

#Наприклад,якщо n дорівнює 12
for num in even_numbers(12):
    print(num, end=" ")

