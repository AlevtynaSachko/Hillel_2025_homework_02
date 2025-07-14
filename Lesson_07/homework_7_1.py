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
            break
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

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

#завдання 5.2 як функція

def update_and_check_people_list(people_list, new_person, indices_for_age_check):
    """
    Оновлює список людей, додаючи нового на початок,
    міняє місцями елементи з індексами 1 і 5 (якщо можливо),
    виводить оновлений список і перевіряє, чи вік людей на заданих індексах >= 30.

    Параметри:
    ----------
    people_list : list of tuples
        Список записів про людей. Кожен запис — це кортеж (ім'я, прізвище, вік, професія, місто).
    new_person : tuple
        Новий запис, який потрібно додати на початок списку.
    indices_for_age_check : list of int
        Індекси, на яких потрібно перевірити, чи вік >= 30.

    Повертає:
    ---------
    None
    (виводить змінений список і результат перевірки віку).
    """
    # 1.Додаємо нового користувача на початок списку
    people_list.insert(0, new_person)

    # 2.Міняємо місцями елементи з індексами 1 і 5, якщо список достатньо довгий
    if len(people_list) > 5:
        people_list[1], people_list[5] = people_list[5], people_list[1]

    #Виводимо змінений список
    print("Оновлений список людей:")
    for index, person in enumerate(people_list):
        print(f"{index}: {person}")

    # 3. Перевіряємо, чи всі люди на заданих індексах мають вік >= 30
    all_ages_ok = all(
        i < len(people_list) and people_list[i][2] >= 30 for i in indices_for_age_check
    )

    print(f"\nЧи всі люди на позиціях {indices_for_age_check} мають вік 30 або більше: {all_ages_ok}")


# Приклад використання:
if __name__ == "__main__":
    список_людей = [
        ('John', 'Doe', 28, 'Engineer', 'New York'),
        ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
        ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
        ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
        ('Michael', 'Brown', 22, 'Student', 'Seattle'),
        ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
        ('David', 'Miller', 33, 'Software Developer', 'Austin'),
        ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
        ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
        ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
        ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
        ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
        ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
        ('Ava', 'White', 42, 'Journalist', 'San Diego'),
        ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
    ]

    нова_людина = ('Alevtyna', 'Sachko', 37, 'QA', 'Hamburg')
    індекси_для_перевірки = [6, 10, 13]

    update_and_check_people_list(список_людей, нова_людина, індекси_для_перевірки)


#Завдання 6.2 як функція

def ask_for_h():
    """
    Запитує у користувача слово, поки воно не міститиме літеру 'h'.

    Програма приймає слово від користувача у нескінченному циклі.
    Якщо в слові є літера 'h' (незалежно від регістру), друкує подяку і завершує виконання.
    Інакше просить спробувати ще раз.

    :return: None
    """
    while True:
        word = input("Введіть слово з літерою 'h': ")
        if 'h' in word.lower():
            print("Дякую, у слові є літера 'h'!")
            break
        else:
            print("На жаль, в цьому слові літера 'h' відсутня. Спробуйте ще раз!")

#викликаємо функцію
ask_for_h()