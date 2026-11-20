from staff_app import Department, Person, Employee, Developer, Manager


def main():
    print("=== 1. Core Hierarchy, Composition & Valid Salary ===")
    engineering = Department("Engineering")
    dev = Developer("Riya", "EMP101", engineering, "Python")
    dev.salary = 65000

    print(dev.describe())
    print("Salary:", dev.salary)
    print("Composition check (dev.department is Department):", isinstance(dev.department, Department))

    try:
        dev.salary = -100
    except ValueError as error:
        print("Validation:", error)

    print("\n=== 2. Extension 1 & 2: Manager Subclass & Department Summary ===")
    mgr = Manager("Aarav", "EMP102", engineering, team_size=8)
    mgr.salary = 95000
    print(mgr.describe())
    print(engineering.summary())

    print("\n=== 3. Extension 3: Blank Name & Negative Value Tests ===")
    try:
        Person("   ")
    except ValueError as error:
        print("Blank name validation:", error)

    try:
        mgr.team_size = -3
    except ValueError as error:
        print("Team size validation:", error)


if __name__ == "__main__":
    main()
