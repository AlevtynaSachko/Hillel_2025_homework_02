#Завдання 6.2 як функція,яку можна протестувати

def contains_h(word: str) -> bool:
   return 'h' in word.lower()

#Завдання 6.3 як функція,яку можна протестувати

def filter_strings_only(lst: list) -> list:
   """Повертає список лише зі строк з вхідного списку."""
   return [item for item in lst if isinstance(item, str)]

#Завдання 6.4 як функція,яку можна протестувати

def sum_even_numbers(lst: list) -> int:
   """
   Повертає суму всіх парних чисел у списку.
   """
   return sum(num for num in lst if num % 2 == 0)

#Завдання 7.1 task 2

def add_numbers(a, b):
   """Повертає суму двох чисел."""
   return a + b

#Завдання 7.1 task 3

def average(numbers):
   if len(numbers) == 0:
      return 0
   return sum(numbers) / len(numbers)

#Завдання 7.1 task 5
def longest_word(words):
   if not words:
      return ""
   return max(words, key=len)