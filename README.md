# MCA Semester I - Practical 7: Inheritance, Composition & Packaging
**Course:** Python & RDBMS
**Student:** Sahil Surendra Shirke  

## Design Note (IS-A, HAS-A, `super()`, Overriding & Properties)
This application models an organizational staff system by combining **IS-A inheritance** with **HAS-A composition** inside a modular `staff_app` Python package[cite: 16, 17]. A two-level inheritance hierarchy (`Person` -> `Employee` -> `Developer` / `Manager`) is used because every `Developer` and `Manager` is a specialized `Employee`, and every `Employee` is a `Person`[cite: 16, 17, 18]. Each subclass calls `super().__init__(...)` to reuse parent initialization and validation logic without duplicating attribute setup[cite: 16, 17]. Polymorphic `describe()` methods override the parent implementation while calling `super().describe()` to preserve a consistent interface and extend output details cleanly[cite: 16, 17].

In contrast, the relationship between `Employee` and `Department` is modeled as **HAS-A composition** (`self.department = department`) rather than inheritance because an employee belongs to a department without being a type of department[cite: 16, 17]. Finally, the `@property` decorator and `@salary.setter` encapsulate `_salary`, ensuring external code accesses `dev.salary` naturally while preventing invalid negative assignments at runtime[cite: 17].

## Extension Task 4: When Composition is Safer Than Inheritance
Composition is safer than inheritance when two classes do not share a true behavioral "is-a" subtype relationship, when you want to avoid tight coupling to a parent class's internal implementation, or when relationships may change dynamically at runtime (such as transferring an `Employee` to a different `Department`).
