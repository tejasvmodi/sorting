def algo(val):
    c=1
    for i in range(1,val+1):
        c= c*i
    return c


i=int(input("enter the number"))
c1=algo(i)
print(c1,end=" ")