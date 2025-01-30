"""
Program Description:
This program turns an inputed string backwards and continues to ask for an input.
When "quit", "Quit", or "q" are inputed, the program stops asking.
"""

string= input("Please enter your string: ")
while string !="quit" and string !="Quit" and string !="q":
    reverse= ''
    for index in range (len(string)-1,-1,-1):
        reverse += string[index]
    print(reverse)
    string= input("\nPlease enter your string: ")