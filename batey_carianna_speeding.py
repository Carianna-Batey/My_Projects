speed_limit=int(input("Please enter the speed limit for the road: "))
car_speed=int(input("Please enter the vehicle's recorded speed: "))
if car_speed<=(speed_limit-10):
    print("The speeding fine is  $50.")
elif (car_speed>=(speed_limit+6))and(car_speed<=(speed_limit+20)):
    print("The speeding find is $75.")
elif (car_speed>=(speed_limit+21))and(car_speed<=(speed_limit+40)):
    print("The speeding fine is $150")
elif car_speed>(speed_limit+40):
    print("The speeding fine is $300")
else:
    print("There is no fine.")