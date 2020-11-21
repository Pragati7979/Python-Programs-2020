class Complex:
    def __init__(self,i,j):
        self.real = i
        self.imaginary = j

    def __add__(self,obj):
        return Complex(self.real + obj.real , self.imaginary+obj.imaginary)

    def __str__(self):
        return(f"{self.real} + {self.imaginary}i")

