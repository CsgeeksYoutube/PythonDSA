class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class CircularLinkedlist:
    def __init__(self):
        self.head = None

    def add_starting(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.ref = new_node
        else:
            new_node.ref = self.head
            temp = self.head
            while( temp.ref != self.head):
                temp = temp.ref
            temp.ref = new_node
        self.head = new_node
    
    def printlinkedlist(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while (n.ref != self.head):
                print(n.data)
                n = n.ref
            print(n.data)

    def add_end(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head = new_node
            new_node.ref = new_node
        else:
            temp = self.head
            while( temp.ref != self.head):
                temp = temp.ref
            temp.ref = new_node
            new_node.ref = self.head

    def add_after(self,data,value):
        if self.head is None:
            print("linked list is empty")
            return
        
        temp = self.head
        while temp.ref!= self.head:
            if value == temp.data:
                break
            temp = temp.ref

        if temp.data != value:
            print("node is not present in linked list")
            return
        
        new_node = Node(data)
        new_node.ref = temp.ref
        temp.ref = new_node

    def add_before(self,data,value):
        if self.head is None:
            print("linked list is empty")
            return
        
        new_node = Node(data)
        if self.head.data == value:
            new_node.ref = self.head
            temp = self.head
            while ( temp.ref != self.head):
                temp = temp.ref
            temp.ref = new_node
            self.head = new_node

        else:
            temp = self.head
            while( temp.ref.data != value):
                temp = temp.ref
                if temp.ref == self.head:
                    print("node is not present in linked list")
                    return
                
            new_node.ref = temp.ref
            temp.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.ref == self.head:
            self.head = None
        else:
            temp = self.head
            while( temp.ref != self.head):
                temp = temp.ref
            self.head = self.head.ref
            temp.ref = self.head

    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.ref == self.head:
            self.head = None
        else:
            temp = self.head
            ptr = temp.ref
            while  ptr.ref != self.head:
                temp = temp.ref
                ptr = ptr.ref

            temp.ref = self.head
        
    def delete_specific_node(self,x):
        if self.head is None:
            print("linked list is empty")
            return

        temp = self.head
        if x == self.head.data:
            if self.head.ref == self.head:
                self.head = None
                return
            else:
                while temp.ref != self.head:
                    temp = temp.ref
            self.head = self.head.ref
            temp.ref = self.head
            return
        while(temp.data != x):
            ptr = temp
            temp = temp.ref
            if temp.ref == self.head and x!= temp.data:
                print("node is not present in linked list")
                return
        ptr.ref  = temp.ref
        temp = None

    def delete_specific_node_after(self,x):
        if self.head is None:
            print("linked list is empty")
            return

        temp = self.head
        while (temp.data != x):
            temp = temp.ref
            if temp.ref == self.head:
                break
        
        if temp.ref == self.head:
            print("can't be deleted")
            return
        elif(temp.ref.ref == self.head):
            temp.ref = self.head
        else:
            ptr = temp.ref
            temp.ref = ptr.ref

    def delete_specific_node_before(self,x):
        if self.head is None:
            print("linked list is empty")
            return
        temp = self.head
        if (temp.ref == self.head or temp.data == x):
            print("node can't be deleted")
            return
        ptr = temp.ref
        if(ptr.data == x and ptr.ref == self.head):
            self.head = self.head.ref
            ptr.ref = self.head
            return
        while(ptr.ref.data != x):
            if(ptr.ref == self.head):
                print("node does not exist")
                return
            ptr = ptr.ref
            temp = temp.ref
        temp.ref = ptr.ref
             

            


        
obj1= CircularLinkedlist()
obj1.add_starting(50)
obj1.add_starting(500)
obj1.add_starting(5000)
obj1.add_end(588)
obj1.add_after(288,500)
obj1.add_before(596,5000)
# obj1.delete_begin()
# obj1.delete_end()
# obj1.delete_specific_node(5000)
# obj1.delete_specific_node_after(50)
obj1.delete_specific_node_before(500)
obj1.printlinkedlist()