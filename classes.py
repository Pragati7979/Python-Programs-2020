class Employee:
    company = "TCS"
    salary = 50000
    def __init__(self):
        print("Initialization of the object of class Employee")

    #First way to change the class variable
    def changeSal(self,sal): 
        self.__class__.sal = sal
        print(f"Salary of the employee is {self.salary} ")

    #Second way of changing the class variable
    @classmethod
    def changeCompany(cls,comp):
        cls.company = comp
        print(f"Employee is working in company {cls.company}")
        
        
e1 = Employee()
e1.changeSal(100)
e1.changeCompany("Google")
