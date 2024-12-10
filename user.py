""" 
Users -
1. Customer
2. Employee
3. Admin
"""

class User:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Employee(User):
    def __init__(self, name, email, phone, address, age, salary, designation):
        super().__init__(name, email, phone, address)
        self.age = age
        self.salary = salary
        self.designation = designation

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.employees = []

    def add_employee(self, name, email, phone, address, age, salary, designation):
        emp = Employee(name, email, phone, address, age, salary, designation)
        self.employees.append(emp)
        print(f"{name} is added")

    def view_employees(self):
        print("Showing Employee List: ")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)

ad = Admin("karim", "karim@gmail.com", 23232323, "Dhaka")
ad.add_employee("rahim", "rahim@gmail.com", 32433434, "Ctg", 45, 12000, "Chef")
ad.add_employee("Sakib", "Sakib@gmail.com", 98989898, "Sylhet", 55, 50000, "Manager")

ad.view_employees()

