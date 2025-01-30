"""
Program Description:
This program returns a list of words and a dictionary sorted by how many times it shows
up in a user-given input.
"""

def build_dictionary(input):
    mydict={}
    word_list = (input.lower()).split(' ') #Makes an object for the list/easier coding
    print(f"\nWord List:\n {word_list}")
            
    for words in word_list:
        if words not in mydict: #Lean on simple functions instead of the complicated ones
            mydict[words] = 1 #set as 1 because its the first time the porgram is seeing the word; Also gives a value
        else:
            mydict[words]+=1 #adds one to the value everytime the word is seen
    return mydict
        

inp=input(':>')
mydict = build_dictionary(inp)#Using an object stores the values to print, if not It wont do anything
sortedk = sorted(mydict.keys())#keys() sorts the values into 
print('\nBag of words:')
for k in sortedk:#solidifies k as the keys
    print(f"{k} - {mydict[k]}")