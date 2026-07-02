# class DataEngineering:    ### Parent class
#     def Course(self):
#         print("Data Engineering Course")
# class Python(DataEngineering): ### child class
#     def Course(self):                   ### Method overriding
#         print("Python Course")
# class Data(DataEngineering): ### child class
#     def Course(self):
#         print("Data Course")

# for x in [Python(), Data()]:  ### Polymorphism
#     x.Course()  ### Method calling








# def add(*args): ### variable-length argument list
#     return sum(args)
# def multiply(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
# def subtract(*args):
#     if len(args) == 0:
#         return 0
#     result = args[0]
#     for num in args[1:]:
#         result -= num
#     return result
# def operate(func, *args):
#     return func(*args)  
# print(operate(add, 1, 2, 3))        # Output: 6
# print(operate(multiply, 1, 2, 3))   # Output: 6
# print(operate(subtract, 10, 5, 2)) # Output: 3

class Vehicle:
    def start_engine(self):
        print("Starting the engine...")
class Car(Vehicle):
    def start_engine(self):
        print("Starting the car engine...")
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Starting the motorcycle engine...")

def initiate_engine(vehicle):
    return vehicle.start_engine()

car = Car()
motorcycle = Motorcycle()

initiate_engine(car)          # Output: Starting the car engine...
initiate_engine(motorcycle)   # Output: Starting the motorcycle engine...









