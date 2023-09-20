list1=[10,20,30,40,50]
print(list1)
i=int(input("enter the value "))
for i1 in list1:
    if(i==i1):
        print("the value is available ",i)
else:
    print("no searching value find")