a=[]
b=[]
c=int(input("how many no.s:"))
i=0
while(i<c):
    d=int(input('position of element :'))
    e=int(input('value of element :'))
    a.insert(d,e)
    b.append(e**2)
    i+=1
print(a)
print(b)
