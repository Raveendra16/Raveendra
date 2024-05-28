class Employee:
    def __init__(self, id, first_name, last_name, position, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class EmploymentManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, id, first_name, last_name, position, salary):
        employee = Employee(id, first_name, last_name, position, salary)
        self.employees.append(employee)

    def remove_employee(self, id):
        for employee in self.employees:
            if employee.id == id:
                self.employees.remove(employee)
                return
        print("Employee not found.")

    def display_employees(self):
        for employee in self.employees:
            print(f"ID: {employee.id}, Name: {employee.full_name()}, Position: {employee.position}, Salary: {employee.salary}")

if __name__ == "__main__":
    ems = EmploymentManagementSystem()
    ems.add_employee(1, "John", "Doe", "Software Engineer", 80000)
    ems.add_employee(2, "Jane", "Doe", "Project Manager", 90000)
    ems.display_employees()
    ems.remove_employee(1)
    ems.display_employees()
