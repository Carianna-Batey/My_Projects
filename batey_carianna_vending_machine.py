"""
Program Description:
This program is a virtual vending machine
Author: Carianna Batey
"""
class VendingMachine:#
    def  __init__(self, soda, coffee, water):#to initialize the variables (tell their number) start w/ init
        self.soda=soda#soda=__ doesnt work in class. you need self first in function and put self.object
        self.coffee=coffee
        self.water=water
    def purchase(self, type):
        if type == 1:
            self.soda-=1
            self.coffee-=1
            self.water-=1
    def restock(self, type, amount):
        if type != 0:
            self.soda+=amount
            self.coffee+=amount
            self.water+=amount
    def inventory(self):
        print('Inventory')
        print(f'Soda: {self.soda} bottles\nCoffee: {self.coffee}\n Water: {self.water}')




machine = VendingMachine(10,10,10)#Made the class, input number of each drink HERE
inp = input(':>')
while inp != 'quit' or inp != 'q':
    if inp=='buy':
        print('Please select an option')
        print('1 - Soda\n2 - Coffee\n3 - Water')
        option=input(':>')
        if option=='1':
            machine.soda-=1
            inventory=VendingMachine.inventory(machine)  
            print('Thank you.')
            
            
        if option=='2':
            machine.coffee-=1
            inventory=VendingMachine.inventory(machine)
            print('Thank you.')
            
            
        if option=='3':
            machine.water-=1
            inventory=VendingMachine.inventory(machine)
            print('Thank you.')
            
    inp = input(':>')
    if inp=='restock':
        print('Please select an option')
        print('1 - Soda\n2 - Coffee\n3 - Water')
        option=input(':>')
        if option=='1':
            amount=int(input('Please enter an amount:'))
            machine.soda+=amount
            inventory=VendingMachine.inventory(machine)  
            print('Thank you.')
            
            
        if option=='2':
            amount=int(input('Please enter an amount:'))
            machine.coffee+=amount
            inventory=VendingMachine.inventory(machine)
            print('Thank you.')
            
            
        if option=='3':
            amount=int(input('Please enter an amount:'))
            machine.water+=amount
            inventory=VendingMachine.inventory(machine)
            print('Thank you.')
    inp = input(':>')
    if inp=='inventory':
        inventory=VendingMachine.inventory(machine)
        print(inventory)