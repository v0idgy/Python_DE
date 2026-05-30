# ## Create a greeter class which greets user as Good Morning, Good Eveneing or Good Night with username.



# from datetime import datetime

# class Greeter:
#     def __init__(self, username):
#         self.username = username

#     def greet(self):
#         current_hour = datetime.now().hour
#         if 5 <= current_hour < 12:
#             greeting = "Good Morning"
#         elif 12 <= current_hour < 18:
#             greeting = "Good Evening"
#         else:
#             greeting = "Good Night"
        
#         return f"{greeting}, {self.username}!"
    
# if __name__ == "__main__":
#     greeter = Greeter("Gourav")
#     print(greeter.greet())



### Create a class of vehicals to store the information of vehical like name, model, year and color. Create a method to display the information of vehical.

# class vehical:
#     def __init__(self, name,model,year,top_speed):
#         self.name = name
#         self.model = model
#         self.year = year
#         self.top_speed = top_speed  

# vehical1 = vehical("BMW", "X5", 2020, 250)
# vehical2 = vehical("Audi", "Q7", 2021, 240)
# vehical3 = vehical("Mercedes", "GLE", 2019, 230)

# print(f"Vehical Name: {vehical1.name}, Model: {vehical1.model}, Year: {vehical1.year}, Top Speed: {vehical1.top_speed} km/h")
# print(f"Vehical Name: {vehical2.name}, Model: {vehical2.model}, Year: {vehical2.year}, Top Speed: {vehical2.top_speed} km/h")
# print(f"Vehical Name: {vehical3.name}, Model: {vehical3.model}, Year: {vehical3.year}, Top Speed: {vehical3.top_speed} km/h")




### Create a bank account class to store the information of bank account like 
# account number, account holder name, balance and interest rate. 
# Create a method to display the information of bank account.

## Create few methods for deposit, withdraw and calculate interest. 


# class BankAccount:
#     def __init__(self, account_number, account_holder_name, balance, interest_rate):
#         self.account_number = account_number
#         self.account_holder_name = account_holder_name
#         self.balance = balance
#         self.interest_rate = interest_rate

#     def display_info(self):
#         return f"Account Number: {self.account_number}, Account Holder: {self.account_holder_name}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate}%"

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")
#             else:
#                 print("Insufficient funds.")
#         else:
#             print("Withdrawal amount must be positive.")

#     def calculate_interest(self):
#         interest = self.balance * (self.interest_rate / 100)
#         print(f"Interest for the current balance is: ${interest:.2f}")

# bank_account = BankAccount("123456789", "Gourav", 1000.00, 5.0)
# print(bank_account.display_info())
# bank_account.deposit(500) 
# bank_account.withdraw(200)
# bank_account.calculate_interest()



## Inheritance Property in OOPs


# class Transport:
#     def start(self):
#         return "Transport is starting."
    
# class Car(Transport):
#     def drive(self):
#         return "Car is driving."
    
# mycar = Car()

# print(mycar.start())  # Inherited method from Transport class
# print(mycar.drive())  # Method from Car class


## Polymorphism in OOPs

# class Shape:
#     def area(self):
#         pass
# class Square(Shape):
#     def area(self):
#         return "Area of Square is side^2"

# class Circle(Shape):
#     def area(self):
#         return "Area of Circle is pi * radius^2"

# shape = [Shape(), Square(), Circle()]
# for s in shape:
#     print(s.area())



## Encapsulation in OOPs

# class User:
#     def __init__(self, name):
#         self.__name = name  # Private attribute
#     def get_name(self):
#         return self.__name

# user1 = User("Gourav")
# print(user1.get_name())  # Accessing private attribute through a public method


## Abstraction in OOPs

# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass













