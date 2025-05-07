print("Hello\nI am an Rent Calculator")

y=input("Do You Like To Calculate your Bill.\n(YES/NO)\n:")
if(y=="yes"):
    print("Please fill these details so I can proceed further.")
    Room=int(input("Enter your Total Room Rent : "))
    Food=int(input("Enter the Amount You used to buy rashan and groceries : "))
    Food_2=int(input("Enter the Amount You used for Snacks OR Food ordering : "))
    Electricity=int(input("How much 'ELECTRICITY UNITS'is been Used: "))
    Electricity_Rate=float(input("What is the rate of Per Unit Electricity Now : "))
    Ebill=(Electricity*Electricity_Rate)
    Fbill=(Food+Food_2)
    total=(Room+Ebill+Fbill)
    print("So,Your total bill would be :",total)
    if(total>=8000):
        print("You need to be More Considerate at Your Expenses from now on !")
    elif(total<=6000):
        print("Great You know Money is an Valueble Asset")
    elif(total<=5500):
        print("Great You are a real Makhi Chuus Insaan")
    else:
        pass;
    print("Do You like to Divide it for 2 person or 3.")
    ok=input("yes OR no ?\n:")
    if ok=="yes":
        d=input("(2/3)\n:")
        if(d=="2"):
            print(total/2)
        elif(d=="3"):
            print(total/3)
    elif ok=="no":
        print("OK,No problem")
    else:
        print("please restart the program by startint point.")
else:
    print("OK,NO PROBLEM.\nI Am Here 24/7 at Your Service.\nConsider to use me.\nAnytime ")
