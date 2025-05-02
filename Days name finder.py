days = int(input("Please enter the no "))
no_of_days=days%7
# % =kyu ki ye remainder leta hai.
if(no_of_days==1):
    print("Monday")
elif(no_of_days==2):
    print('Tuesday')
elif(no_of_days==3):
    print('Wednesday')
elif(no_of_days==4):
    print('Thursday')
elif(no_of_days==5):
    print('Friday')
elif(no_of_days==6):
    print('Saturday')
elif(no_of_days==0):
    print('Sunday')
elif(no_of_days==str):
    print("Given value isn't in 'Numbers'.")
else: 
    print("Given value isn't in 'Numbers'.")

