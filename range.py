#Range==
'''for i in range(2,9,1):#FOR LOOP
 print(i)'''

'''r1=range(2,9,1)#WHILW LOOP
i=0
while(i<7):
    print(r1[i])
    i+=1
#WAP T0 PRINT 1ST 10 odd  NATURAL NUMBERS
for i in range(1,21,2):
    print(i)
#WAP TO PRINT 1ST  NATURAL NUMBERS WHERE N IN GIVEN BY USER

n=int(input('i want only these natural num'))
for i in range (1,n+1):
 print(i)
# WAP TO PRINT 1ST EVEN NATURAL NUMBERS WHERE N IN GIVEN BY USER
n=int(input('i want only these even num'))
for i in range (2,n+n+1,2):
 print(i)
#WAP TO PRINT ELEMENTS OF ABOVE QUES IN HORIZONTAL LINE
n=int(input('i want only these even num'))
for i in range (2,n+n+1,2):
 print(i,end=' ')
x=int(input("no"))
a=range(100,1000)
if(x in a):
    print("Yes")
else:
    print("No")
'''
x=int(input("no"))
if((x >100) and (x<999)):
    print("Yes")
else:
    print("No")
