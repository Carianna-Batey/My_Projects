#this checks the validity of the interstates
state_number=int(input("Please enter an interstate number: "))
if state_number%100==00:
    print(f"{state_number} is not a valid interstate number.")
elif (state_number>=1)and(state_number<=99)and(state_number%2==0):
    print(f"I-{state_number} is a primary, going east/west.")
elif (state_number>=1)and(state_number<=99)and(state_number%2==1):
    print(f"I-{state_number} is a primary, going north/south.")
elif (state_number>99)and(state_number%2==0):
    print(f"I-{state_number} is auxilary, serving I-{state_number%100}, going east/west.")
elif (state_number>99)and(state_number%2==1):
    print(f"I-{state_number} is auxilary, serving I-{state_number%100}, going north/south.")