class Employee:
    def __init__(self, *, name, salary, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, *, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, *, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, *, name, salary, department, programming_language, team_size):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )
        self.team_size = team_size


# Тестуємо
if __name__ == "__main__":
    tl = TeamLead(
        name="Олексій",
        salary=75000,
        department="IT",
        programming_language="Python",
        team_size=7
    )

    print(tl.name, tl.salary, tl.department, tl.programming_language, tl.team_size)
    # Перевірки типів
    print(isinstance(tl, Employee)) # True
    print(isinstance(tl, Manager)) # True
    print(isinstance(tl, Developer)) # True
    print(isinstance(tl, TeamLead)) # True