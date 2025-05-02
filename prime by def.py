'''
def square ():
    a=int(input('hell no'))
    x=(a*a)
    
    return x
print(square())

'''

def prime(x):
    status=1
    for i in range(2,x):
        if x%i==0 :
            status=0
            break
    if(status==1):
        print('prime')
    else:
        print("not prime")

prime(x=int(input('enter the nuumber :')))
