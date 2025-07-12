# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break # зупиняємо цикл, якщо добуток перевищує 25
        print(str(number) + " x " + str(multiplier) + " = " + str(result))
        multiplier += 1

multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_numbers(a, b):
    return a + b
print(add_numbers(7, 8))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
print(average([10, 20, 30]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]
print(reverse_string("Illumination!!!"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    if not words:
        return ""
    return max(words, key=len)
print(longest_word(["we", "are", "the", "champions"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

