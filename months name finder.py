month = int(input("please enter the no "))
No_of_month=month%12
# % =kyu ki ye remainder leta hai.
if(No_of_month==1):
    print("january")
elif(No_of_month==3):
    print('march')
elif(No_of_month==4):
    print('april')
elif(No_of_month==5):
    print('may')
elif(No_of_month==6):
    print('june')
elif(No_of_month==7):
    print('july')
elif(No_of_month==8):
    print('august')
elif(No_of_month==9):
    print('september')
elif(No_of_month==10):
    print('october')
elif(No_of_month==11):
    print('november')
elif(No_of_month==0):
    print('december')
elif(No_of_month==2):
    print('february')
else: 
    print("given value isn't in numbers.")
