from .department import Department


class Person:
    def __init__(self, name):
        if not name or not str(name).strip():
            raise ValueError("Name cannot be blank")
        self.name = str(name).strip()

    def describe(self):
        return f"Person: {self.name}"


class Employee(Person):
    def __init__(self, name, employee_id, department):
        super().__init__(name)
        self.employee_id = str(employee_id).strip()
        if not isinstance(department, Department):
            raise TypeError("department must be a Department object")
        self.department = department
        self._salary = 0.0
        self.department.add_member(self)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = float(amount)

    def describe(self):
        return (
            f"Employee: {self.name}, ID: {self.employee_id}, "
            f"Department: {self.department}"
        )


class Developer(Employee):
    def __init__(self, name, employee_id, department, language):
        super().__init__(name, employee_id, department)
        self.language = str(language).strip()

    def describe(self):
        return (
            f"{super().describe()}, "
            f"Role: Developer, Language: {self.language}"
        )


class Manager(Employee):
    def __init__(self, name, employee_id, department, team_size=0):
        super().__init__(name, employee_id, department)
        self._team_size = 0
        self.team_size = team_size

    @property
    def team_size(self):
        return self._team_size

    @team_size.setter
    def team_size(self, count):
        if not isinstance(count, int) or count < 0:
            raise ValueError("Team size must be a non-negative integer")
        self._team_size = count

    def describe(self):
        return (
            f"{super().describe()}, "
            f"Role: Manager, Team Size: {self.team_size}"
        )
