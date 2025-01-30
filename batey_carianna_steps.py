"""
Carianna Batey
Program Description:
This program converts distance in feet to the average human step
"""
x= float(input("Please enter the distance travelled in feet: "))
def feet_to_steps():
    steps=x/2.5
    print(f"{steps:.0f} steps")
feet_to_steps()