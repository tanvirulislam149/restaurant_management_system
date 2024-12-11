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

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = None

    def show_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name):
        item = restaurant.menu.find_item(item_name)
        if item:
            pass
        else:
            print("Item not found")

    def view_cart(self):
        print("--------View cart---------")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.item.items():
            print(f"{item.name} {item.price} {quantity}")
        print(f"Total price: {self.cart.total_price}")

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.employees = []

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employees()

    def add_menu_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)

    def show_menu(self, restaurant):
        restaurant.menu.show_menu()

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []     # employees er database
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} is added")

    def view_employees(self):
        print(f"------------Showing Employee List of {self.name} restaurant------------")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)
    
class Menu:
    def __init__(self):
        self.items = []
    
    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for i in self.items:
            if i.name.lower() == item_name.lower():
                return i
            else:
                return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted")
        else:
            print("Item not found")
        
    def show_menu(self):
        print("--------Menu------------")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

ad = Admin("karim", "karim@gmail.com", 23232323, "Dhaka")
dine = Restaurant("dine")
sakib = Employee("Sakib", "Sakib@gmail.com", 98989898, "Sylhet", 55, 50000, "Manager")
ad.add_employee(dine, sakib)
rahim = Employee("rahim", "rahim@gmail.com", 32433434, "Ctg", 45, 12000, "Chef")
ad.add_employee(dine, rahim)
ad.view_employee(dine)
item1 = FoodItem("Pizza", 12, 40)
item2 = FoodItem("Burger", 112, 20)
item3 = FoodItem("Biri", 312, 30)

ad.add_menu_item(dine, item1)
ad.add_menu_item(dine, item2)
ad.add_menu_item(dine, item3)

ad.show_menu(dine)
