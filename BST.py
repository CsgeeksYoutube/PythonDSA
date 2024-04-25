class BinaryST:
    def __init__(self,data):
        self.data = data
        self.lchild= None
        self.Rchild= None
    
    def insertvalue(self,value):
        if self.data is None:
            self.data = value
            return
        
        if self.data > value:
            if self.lchild:
                self.lchild.insertvalue(value)
            else:
                self.lchild=BinaryST(value)
        else:
            if self.Rchild:
                self.Rchild.insertvalue(value)
            else:
                self.Rchild=BinaryST(value)

    def preorder(self):
        print(self.data)
        if self.lchild:
            self.lchild.preorder()
        if self.Rchild:
            self.Rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data)
        if self.Rchild:
            self.Rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.Rchild:
            self.Rchild.postorder()
        print(self.data)

    def search(self,value):
        if self.data == value:
            print("Node is Found")
            return
        if value < self.data:
            if self.lchild:
                self.lchild.search(value)
            else:
                print("Node does not exist")
        else:
            if self.Rchild:
                self.Rchild.search(value)
            else:
                print("Node does not exist")
            
    def delete(self,value):
        if self.data is None:
            print("Tree is empty")
            return
        
        if value < self.data:
            if self.lchild:
                self.lchild = self.lchild.delete(value)
            else:
                print("node is not present in the tree")
        
        elif value > self.data:
            if self.Rchild:
                self.Rchild = self.Rchild.delete(value)
            else:
                print("node is not present in the tree")

        else:
            if self.lchild is None:
                temp = self.Rchild
                self = None
                return temp
            
            if self.Rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.data = node.data
            self.Rchild = self.Rchild.delete(node.data)
        return self
            


root = BinaryST(58)
nodevalue = [10,45,96,11,115,859,47,100]
for i in nodevalue:
    root.insertvalue(i)
root.inorder()
root.delete(47)
# root.search(8598)
# print(root.data)
# print(root.lchild.Rchild.data)
# print(root.Rchild.data)
# root.postorder()
root.inorder()

