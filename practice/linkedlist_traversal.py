class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

class Sll:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("list is empaty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next

n1=Node(5)
sll=Sll()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4
sll.traversal()