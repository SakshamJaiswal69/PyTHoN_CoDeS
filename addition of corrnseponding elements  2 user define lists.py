a=[]
b=[]
c=[]
d=int(input("How many no you want to put ?"))
i=0
while(i<d):
    e=int(input("Enter the no in first list :"))
    a.append(e)
    i=i+1
j=0
while(j<d):
    f=int(input("Enter the no in second list:"))
    b.append(f)
    j+=1
k=0
while(k<d):
    sum=(a[k]+b[k])
    c.append(sum)
    k+=1
print(c)
