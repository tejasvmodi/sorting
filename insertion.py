a=[100,450,30,400,230]

for i in range(len(a)):
    temp=a[i]
    k=i-1
    while(k>=0 and a[k]>temp):
        a[k+1]=a[k]
        k=k-1
        print(a,"\n")
    a[k+1]=temp
    print(a)
    
