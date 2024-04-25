
class CreateNode:
    def __init__(self,data):
        self.data = data
        self.lchild= None
        self.rchild= None
        self.height= 1


class AVL_Tree:
    def insert(self,root,key):
        if not root:
            return CreateNode(key)
        
        elif key < root.data:
            root.lchild = self.insert(root.lchild, key)
        else:
            root.rchild = self.insert(root.rchild,key)
        
        root.height = 1 + max(self.getHeight(root.lchild),
                             self.getHeight(root.rchild))
        
        balance = self.getBalance(root)

        if balance > 1 and key < root.lchild.data:
            return self.clockwiserotation(root)
 
        if balance > 1 and key > root.lchild.data:
            root.lchild = self.anticlockwiserotation(root.lchild)
            return self.clockwiserotation(root)
        
        if balance <-1 and key > root.rchild.data:
            return self.anticlockwiserotation(root)
        
        if balance < -1 and key < root.rchild.data:
            root.rchild = self.clockwiserotation(root.rchild)
            return self.anticlockwiserotation(root)
        
        return root

    def anticlockwiserotation(self, ptr):
        temp = ptr.rchild
        temp1 = temp.lchild

        temp.lchild = ptr
        ptr.rchild = temp1

        ptr.height = 1 + max(self.getHeight(ptr.lchild),
                             self.getHeight(ptr.rchild))
        temp.height = 1 + max(self.getHeight(temp.lchild),
                             self.getHeight(temp.rchild))
        
        return temp

    
    def clockwiserotation(self,ptr1):
        temp2 = ptr1.lchild
        temp3= temp2.rchild

        temp2.rchild = ptr1
        ptr1.lchild = temp3

        ptr1.height = 1 + max(self.getHeight(ptr1.lchild),
                             self.getHeight(ptr1.rchild))
        temp2.height = 1 + max(self.getHeight(temp2.lchild),
                             self.getHeight(temp2.rchild))
        
        return temp2
    
    def delete(self,root,key):
        if not root:
            return root
        
        elif key < root.data:
            root.lchild = self.delete(root.lchild, key)

        elif key > root.data:
            root.rchild = self.delete(root.rchild, key)

        else:
            if root.lchild is None:
                temp = root.rchild
                root = None
                return temp
            elif root.rchild is None:
                temp = root.lchild
                root = None
                return temp
            
            temp = self.getMinValue(root.rchild)
            root.data = temp.data
            root.right = self.delete(root.rchild,temp.data)
        
        if root is None:
            return root
        
        root.height = 1 + max(self.getHeight(root.lchild),
                             self.getHeight(root.rchild))
        
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.lchild) >= 0:
            return self.clockwiserotation(root)
        if balance > 1 and self.getBalance(root.lchild) < 0:
            root.lchild = self.anticlockwiserotation(root.lchild)
            return self.clockwiserotation(root)
        
        if balance < -1 and self.getBalance(root.rchild) <= 0:
            return self.anticlockwiserotation(root)
        if balance < -1 and self.getBalance(root.rchild) > 0:
            root.rchild = self.clockwiserotation(root.rchild)
            return self.anticlockwiserotation(root)
        
        return root
            


    def getMinValue(self, root):
        if root is None or root.lchild is None:
            return None
        return self.getMinValue(root.lchild)

    def getHeight(self,root):
        if not root:
            return 0
        
        return root.height
    
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.lchild) - self.getHeight(root.rchild)

    def preorder(self,root):
        if not root:
            return
        print("{0} ".format(root.data), end = " ")
        self.preorder(root.lchild)
        self.preorder(root.rchild)
    
mytree = AVL_Tree()
root = None
values  = [9,4,8, 6, 11, 16, 1, 2]
for val in values:
    root = mytree.insert(root,val)

print("preorder of avl tree")
mytree.preorder(root)
print()

key= 6
root = mytree.delete(root, key)
print("preorder of avl tree after deletion")
mytree.preorder(root)
print()