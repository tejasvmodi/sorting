class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkList:
    def __init__(self):
         self.head = None

    def InsertNode(self, value):
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            newNode.prev=None
            newNode.next=None
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            newNode.prev = temp
            temp.next = newNode

    def forwardprint(self):
        if self.head == None:
            print("List is Empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data,end=" ")
                temp = temp.next

    def backwordPrint(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            while temp != None:
                print(temp.data,end=" ")
                temp = temp.prev

    def count(self):
        if self.head == None:
            print("List is empty")
        else:
            count = 0
            temp = self.head
            while temp != None:
                count = count + 1
                temp = temp.next

            print("count of the item in list is", count)
    
    def search(self,val):
        if self.head == None:
            print("List is empty ")
        else:
            temp=self.head
            flag=0
            while temp != None :
                if temp.data == val :
                    print ("value search")
                    flag=1
                temp=temp.next
                
            if flag==0 :
                print("value not in list ")


    def insertAfter(self,key,value):
        newNode=Node(value)
        if self.head == None:
            self.head = newNode
            newNode.prev=None
            newNode.next=None
        else:
            temp=self.head
            while temp != None :
                if temp.data == key :
                    newNode.next = temp.next
                    newNode.prev=temp
                    temp.next=newNode
                
                temp=temp.next
        
    def insertBefore(self,key,value):
        newNode=Node(value)
        if self.head == None:
            self.head = newNode
            newNode.prev=None
            newNode.next=None
        else:
            if self.head.data==key :
                newNode.prev = None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            else:
                temp= self.head
                while temp.next != None and temp.next.data!=key:
                    temp= temp.next

                if temp.next!=None :
                    newNode.next = temp.next
                    newNode.prev= temp
                    temp.next.prev=newNode
                    temp.next=newNode
                    
                    
    def deletebyKey(self,key):
        if self.head==None:
            print ("List is empty ")
        else:
            if self.head.data==key :
                temp=self.head
                self.head=self.head.next
                self.head.prev=None
                del temp
            else:
                temp = self.head
                while temp != None :
                    if temp.data == key:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                        del temp
                        break
                    temp=temp.next
                else:
                    print("no value deleted in list ")
                
    
    def deletebyposition(self, position):
        if self.head == None:
            print("List is empty")
        else:
            if position == 1:
                temp = self.head
                self.head = self.head.next
                if self.head != None:
                    self.head.prev = None
                del temp
            else:
                temp = self.head
                current_position = 1

                while current_position < position and temp != None:
                    temp = temp.next
                    current_position += 1

                if temp == None:
                    print(f"Position {position} is out of bounds")
                else:
                    if temp.prev !=None:
                        temp.prev.next = temp.next
                    if temp.next != None:
                        temp.next.prev = temp.prev
                    print("the value is deleted")
                    del temp

dll=DoublyLinkList()
while True:
    print()
    print("1 Insert the node")
    print("2 Forward Print")
    print("3 Backword print")
    print("4 Count the item in list")
    print("5 search the item in list")
    print("6 insert after the")
    print("7 insert before the")
    print("8 Delete by key")
    print("9 Delete by position")
    print("10 exit")
    choice=int(input("enter your choice "))
    match choice:
        case 1:
            c=int(input("Number of element "))
            for i in range(0,c):
                i=input("Enter the value ")
                dll.InsertNode(i)
            print()
            
        case 2:
            print()
            dll.forwardprint()
            print()
            
        case 3:
            print()
            dll.backwordPrint()
            print()
            
        case 4:
              print()
              dll.count()
              print()
             
        case 5:
            print()
            i=input("Enter the value ")
            dll.search(i)
            print()
            
        case 6: 
             print()
             k=input("Enter the value from list ")
             i=input("Enter the value ")
             dll.insertAfter(k,i)
            
             print()
        case 7:
              print()
              k=input("Enter value from list ")
              i=input("Enter the value ")
              dll.insertBefore(k,i)
             
              print()
        case 8:
             print()
             i=input("Enter the value ")
             dll.deletebyKey(i)
           
             print()
        case 9:
             print()
             i=int(input("Enter the position "))
             dll.deletebyposition(i)
            
             print()
        case 10: 
            exit()
        case default:
            print()
            print()
            print("Please select the number between 1 to 10")
            exit()



                


        
