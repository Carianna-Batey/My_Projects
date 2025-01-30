password= input("Please Enter Your Password: ")
password_strong= ""#"" is for strings, {}is for dictionary, [] is for lists and values
#always make an empty slot when replacing characters, numbers, values
for char in password:
    if char =='o':#char is okay to leave by itself
       password_strong+='0'
    elif char =='i':
        password_strong+='1'
        # all
    elif char == 'a':
        password_strong += '@'
    elif char == 'e':
        password_strong += '3'
    elif char == 'A':
        password_strong += '4'
    elif char == 'B':
        password_strong += '8'
    elif char == 's':
        password_strong += '$'
    else:
        password_strong+=char
password_strong+='!'#append is only for lists, use += for strings
print(f"Your new strong password is: {password_strong}")
