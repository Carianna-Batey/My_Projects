import math
radius=int(input("Please enter the radius of the sphere: "))
volume=4/3*math.pi*radius**3
print(f"The volume of a sphere with the radius of {radius} is {volume:.2f}.")
factorial=math.factorial(radius)
print(f"\nThe factorial of {radius} is {factorial}")