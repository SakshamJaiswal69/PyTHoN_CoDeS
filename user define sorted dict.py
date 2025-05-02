'''
d1={}
a=0
i=int(input("how many ?"))
while(a<i):
    xx=input('key :')
    xy=input('data :')
    d1[xx]=xy
    a+=1
    b=[]
    for j in d1:
        b.append(j)
        print(sorted(b))

    '''
d1={}
i=int(input("how many ?"))
for a in range(0,i):
    d1[(input('key'))]=(input("data"))
    b=[]
    for j in d1:
        b.append(j)
    for r in sorted(b):
        
        print (r)
