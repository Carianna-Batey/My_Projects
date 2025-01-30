"""
Program Description:
This program converts number of steps into how many miles, with automated responses for incorrect inputs
Author: Carianna Batey
"""
class NegativeValueError(Exception):
    def __init__(self,message):
        self.message=message


def steps_to_miles(num_steps):
    miles= (num_steps/2000)
    if num_steps<0:
        raise NegativeValueError('Exception: Negative Step Count Entered.')
    else:
        return (f'{miles:.2f} miles')


try:
    num_steps=int(input('Enter # of steps:>'))
    print(steps_to_miles(num_steps))
    
except ValueError:
    print('Exception: Non-Numeric Value Entered.')
    
except NegativeValueError:
    print('Exception: Negative Step Count Entered.')
    