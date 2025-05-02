def palin():
    str=(input("type the word you want to check : "))
    if(str==str[::-1]):
        print("String is palindrome")
    else:
        print("String is Not palindrome")

palin()
