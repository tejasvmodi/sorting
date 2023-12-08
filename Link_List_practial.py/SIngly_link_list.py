class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkList:
    def __init__(self):
        self.head=None
    
    def insert(self,value):
        newNode=Node(value)

        if self.head==None:
            self.head=newNode
            newNode.next=None
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=newNode
            
            
    def insertbefore(self,value,key):
        newNode=Node(value)

        if(self.head==None):
            self.head=newNode
        else:
            temp=self.head
            if temp.data==key:
                newNode.next=temp
                self.head=newNode
            else:
                while temp.next!=None:
                    if temp.next.data == key:
                        newNode.next=temp.next
                        temp.next=newNode
                        return
                    temp=temp.next
                    
                temp.next=newNode

    
    def display(self):
        if self.head==None:
            print ("List is empty ")
        else:
            temp=self.head
            while temp!= None :
                print(temp.data,end=" ",)
                temp=temp.next           
            print() 



def main():
    c= SingleLinkList()
    while True:
        choice=int(input("Enter the choice"))
        match choice:
            case 1:
                i=int(input("enter the value "))
                c.insert(i)
                c.display()
            case 2:
                c.display()
            case 3:
                i=int(input("enter the number "))
                p=int(input("enter the previous number "))
                c.insertbefore(i,p)
                c.display()
            case 10:
                exit()
main()