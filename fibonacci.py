def fibo(val):
    if val <=1 :
        return 1
    else:
        
        return fibo(val-1)+fibo(val-2)
    

a=int(input("enter the number"))
c=0
for i in range(a,0,-1):
    c=fibo(i)
    # print(i)
    print(c,end=" ")