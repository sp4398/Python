class node:
    def __init__(self,num):
        self.lchild=None
        self.data=num
        self.rchild=None 

class tree:
    def __init__(self):
        self.root=None 
    def insert(self,n):
        newnode=node(n)
        if self.root==None:
            self.root=newnode
        else:
            temp=self.root
            while temp!=None:
                if n<temp.data:
                    if temp.lchild==None:
                        temp.lchild=newnode
                        return
                    else:
                        temp=temp.lchild
                if n>temp.data:
                    if temp.rchild==None:
                        temp.rchild=newnode
                        return
                    else:
                        temp=temp.rchild
        


