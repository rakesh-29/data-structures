class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singelell:

    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    def traverse(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

ll=singelell()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.traverse()

