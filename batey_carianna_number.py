"""
Program Description:
This program calculates numbers with a class system
Author: Carianna Batey
"""
class Number:
    def __init__(self,number):
        self.number= number
    def __str__(self):
        return str(self.number)
    def __add__(self,other):
        return Number(self.number + other.number)
    def __sub__(self,other):
        return Number(self.number - other.number)
    def __mul__(self,other):
        return Number(self.number * other.number)
    def __truediv__(self,other):
        return Number(self.number // other.number)

a=Number(25)
b=Number(5)

c = a / b

print(c)