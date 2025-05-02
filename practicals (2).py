'''
# Write a program to print cube of a number given by user
a= int(input("enter a number :"))
b=(a**3)
print(b)
'''
'''
#Write a program to take the percentage of a student and prints its grade according to below criteria: -
#Grade A greater than 90, 
#Grade B greater than 80, 
#Grade C greater than 70, 
#Grade D greater than 60, 
#Grade E greater than 50,
#Grade F means fail,
a=int(input("enter the percentage please :"))
if(a>=90):
    print("great job you obtained \n grade A")
elif(a>=80):
    print("great job you obtained \n grade B")
elif(a>=70):
    print("nice great job you obtained \n grade C")
elif(a>=60):
    print("You obtained \n grade D")
elif(a>=50):
    print("you obtained \n grade E")
elif(a<50):
    print("you obtained\n grade F")
else:
    print("please re-enter the data")
'''

'''
# Write a program to print the multiplication of three numbers given by user.

a=int(input("enter first no :"))
b=int(input("enter second no :"))
c=int(input("enter third no :"))
d=(a*b*c)
print(d)
'''
'''
#Write a python program to count the number of even and odd numbers from a series of numbers givenby user.
a=int(input("enter the last digit of the series :"))
d=[]

for i in range(1,a+1):
    d.append(i)
even=0
odd=0

for j in d :
    if j%2==0:
        even=even+1
    else:
        odd=odd+1
print("No.of even no :",even)
print("No.of even no :",odd)
'''
"""
# Write a program to print first 10 natural numbers by using while loop.
a=1
while(a<=10):
    
    print(a)
    a+=1
"""
"""
a=1
for a in range(1,101):
    print(a**2)
"""
'''
#Write a program to accept three different numbers from user and find which is greater.
a=int(input("enter first no :"))
b=int(input("enter second no :"))
c=int(input("enter third no :"))
if (a>b)and(a>c):
    print(a,"is the greatest No.")
if(a<b)and(b>c):
    print(b,"is the greatest No.")
if(a<c)and(b<c):
    print(c,"is the greatest No.")
'''
"""

def fact2(n):
    if(n==1):
        return 1
    else:
        return(n*fact2(n-1))
print(fact2(5))
"""
"""
a=int(input("enter how many no you want to put:"))
c=[]
for i in range(a):
    b=int(input("enter the list elements"))
    c.append(b)
print(max(c))
print(min(c))
"""
'''
##

#Write a python program to calculate electricity bill according to given criteria: 
#1 - 100 unit - 1.5/= 
#101-200 unit - 2.5/= 
#201-300 unit - 4/= 
#Above 300 unit - 10/=
a=float(input("enter the units to calculate : "))
if (a<100):
    b=()
    print("your electricity bill is :" ,a*1.5)
elif(100<a<=200):
    print("your electricity bill is :" ,a*2.5)
elif(200<a<=300):
    print("your electricity bill is :" ,a*4)
elif(a>300):
    print("your electricity bill is :" ,a*10)
else:
    print("given data is not in digits")

'''
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
# Write a program to take different words separated by comma and  print reverse order
# of their occurrence.
n=int(input("enter how many no you want to put:"))
a=0
b=1
c=0
for i in range (n):
    c=(b+a)
    a=b
    b=c
    print(c)
'''
a=20
b=10
c=14
d=4
e=0
f=True
g=False
#print(e=(a+b)*c/d**2 and c>=4)
print (30*14/16 and 14>=4)
#e=(a+b) or c/d**2 and c<4
print(20+10 or 14/16 and 14<4)
#e=a+(b*c)/d or g or f
print(20+140/4 or g or f)
#. e=not a+(b*c)-d or g or f
print(not a + 140-4 or g or f )
#. e=a|(b*c)^d-e
# e=a==7 and b==7
print(a==7 and b==7)
#e=not(a==b and b==c)
print(not (a==b and b==c))
#d=d>>2
print(f)
#f=a!=b and d>e or True
print(a!=b and d>e or True)
#=2*3**4-b-e
print(2*3**4-b-e)
