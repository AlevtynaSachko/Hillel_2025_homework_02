class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        """Метод для зміни середнього балу"""
        self.average_grade = new_grade

    def info(self):
        """Метод для виведення даних"""
        return (f"Студент: {self.first_name} {self.last_name}, "
                f"Вік: {self.age}, "
                f"Середній бал: {self.average_grade}")


# створюємо об’єкт класу
student1 = Student("Кароліна", "Ферейра", 23, 85)

print(student1.info())

# змінюємо середній бал
student1.update_average_grade(93)

print(student1.info())