age=int(input("Please enter your age; "))
weight=int(input("Please enter your weight: "))
heart_rate=int(input("Please enter your heart rate in beats per minute: "))
time=int(input("Please enter your workout time in minutes: "))
calories_burned=((age*0.2757+weight*0.03295+heart_rate*1.0781-75.4991)*time)/8.368
print(f"Calories burned: {calories_burned:.2f}")