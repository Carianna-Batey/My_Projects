num_values= int(input("Please enter the number of floating-point values: "))
values=[]
for i in range(0,num_values):
    float_=float(input("Please enter the floating-point value: "))
    values.append(float_)
print("\nNormalized Floating-Point Values:")
for val in values:
        normalized= val/max(values)
        print(f'{normalized:.2f}')