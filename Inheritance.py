class Person:
    def __init__(self):
        print("Initialize the object of class Person")
    @staticmethod
    def greet():
        print("Person is saying hii")

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Initialize the object of class Employee")
    def greet(self):
        super().greet()
        print("Employee is saying hii to you!!")
    
