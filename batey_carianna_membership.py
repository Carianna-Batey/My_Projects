vowels=["a", "e", "i", "o", "u"]
digits=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
punctuation=[",", ";", ".", "?", "!"]
character=input("Please enter a character: ")
if character in digits:
    print(f"The character '{character}' is a digit.")
if character in punctuation:
    print(f"The character '{character}' is punctuation.")
if character in vowels:
    print(f"The character '{character}' is a vowel.")
elif character not in vowels and character not in digits and character not in punctuation:
    print(f"The character '{character}' is a consonant.")