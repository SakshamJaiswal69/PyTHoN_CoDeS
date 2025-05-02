def Armstrong(n=int(input('enter the number : '))):
    sum=0
    order=len(str(n))
    num=n
    while(n>0):
        digit=n%10
        sum+=digit**order
        n=n//10
    
    if(sum==num):
        print("given input is an Armstrong number")
    else:
        print("given input is not an Armstrong number")
Armstrong()
