a=[10,40,50,60,70]
for i in range(len(a)-1):
    small=i
    for j in range(i+1,len(a)):
        if(a[j]<a[small]):
            small=j
    temp=a[i]
    a[small]=a[i]
    a[i]=temp


print(a)

    