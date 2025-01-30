"""
Carianna Batey
Program Description:
This program filters an input string and removes the banned words
"""
banned_words={"Turkey", "Dog", "Fox", "Cat", "Chicken"}
def text_filter(message):
    output=""
    words=message.split()
    for word in words:
        if word not in banned_words:
            output+=word+" "
    return output

if __name__ == "__main__":
    message=input(">: ")
    print("Input Message:", message)
    print("Output Message:", text_filter(message))