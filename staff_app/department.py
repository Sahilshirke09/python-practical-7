class Department:
    def __init__(self, name):
        if not name or not str(name).strip():
            raise ValueError("Department name cannot be blank")
        self.name = str(name).strip()
        self._members = []

    def add_member(self, employee):
        if employee not in self._members:
            self._members.append(employee)

    def summary(self):
        return f"Department: {self.name} | Total Staff: {len(self._members)}"

    def __str__(self):
        return self.name
