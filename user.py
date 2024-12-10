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

