
'''
#Write a program to print the sum of first n natural numbers by using recursive function
def findsum(x):
    if (x==0):
        return 0
    else:
        return x+findsum(x-1)

a=int(input('enter the last natural number : '))
print("the sum of the n natural number is : " ,findsum(a))

'''
'''
# Write a program to write data into a file and print its content on console.
a=input("enter the line or word or a paragragh you want to write :")
f1=open('my text.txt',"w+")
f1.write(a)
f1.seek(0)
print(f1.read())
'''
'''
# Write a program to print the multiplication table of a number given by user.
a=int(input("enter the digit you want the multiplication table of :"))
for i in range(1,11):
      print(a*i)
'''
'''
# fibnocii wala
n=int(input("enter how many no you want to put:"))
a=0
b=1
c=0
for i in range (n):
    
    print(c)
    a=b
    b=c
    c=a+b
''' 
