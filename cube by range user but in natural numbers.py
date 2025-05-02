'''
a=[]
n=int(input("no"))
for i in range (1,n+1):
    a.append(i**3)
print(a)
'''
a=[]
n=int(input("no"))
i=0
b=range(1,n+1)
while(i<n):
    c=b[i]**3
    a.append(c)
    i+=1
print(a)
