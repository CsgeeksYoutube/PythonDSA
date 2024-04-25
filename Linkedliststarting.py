class Node:
    def __init__(self,data):
        self.data= data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add_starting(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def printlinkedlist(self):
        if self.head is None:
            print("linked is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.ref is not None:
                temp = temp.ref
            temp.ref = new_node
    def add_after(self, data, value):
        temp = self.head
        while temp is not None:
            if value == temp.data:
                break
            temp = temp.ref
        if temp is None:
            print("node is not found in linked list")
        else:
            new_node = Node(data)
            new_node.ref = temp.ref
            temp.ref = new_node

    def add_before(self,data,value):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.data == value:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        temp = self.head
        while(temp.data != value):
            ptr = temp
            temp = temp.ref
            if temp is None:
                print("node is not found in linked list")
                break
        if temp is not None:
            new_node = Node(data)
            new_node.ref = temp
            ptr.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print('linked list is empty')
        else:
            temp = self.head
            self.head = self.head.ref
            temp = None
    def delete_end(self):
        if self.head is None:
            print('linked list is empty')
        elif self.head.ref is None:
            self.head = None
        else:
            temp = self.head
            ptr = temp.ref
            while ptr.ref is not None:
                temp = temp.ref
                ptr= ptr.ref
            temp.ref = None

    def delete_specific_node(self,x):
        if self.head is None:
            print("cant be delete")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        temp = self.head
        while (temp.data != x):
            ptr = temp
            temp = temp.ref
            if (temp is None):
                print("Node is not available")
                # return ki jagah break nhi aaega
                return
        ptr.ref = temp.ref
        temp = None
        
    def delete_specific_node_after(self,x):
        if self.head == None:
            print("cant be deleted")
            return
        temp = self.head
        while( temp.data != x):
            temp = temp.ref
            if (temp is None):
                print("Node is not available")
                return
        if temp.ref is None:
            print("cant be deleted")
            return
        elif(temp.ref.ref is None):
            ptr = temp.ref
            temp.ref = None
        else:
            ptr = temp.ref
            temp.ref = ptr.ref
            ptr = None

    def delete_specific_node_before(self,x):
        if self.head == None:
            print("can't delete the node")
            return
        temp = self.head
        ptr = temp.ref
        if(ptr is None or temp.data == x):
            print("can't delete")
            return
        if(ptr.data == x):
            self.head = self.head.ref
            return
        if(ptr.ref is None):
            print("node does not exist")
            return
        while(ptr.ref.data !=x):
            ptr = ptr.ref
            temp = temp.ref
            if(ptr.ref is None):
                print("node does not exist")
                return
        temp.ref = ptr.ref
        ptr = None


    

obj1 = Linkedlist()
obj1.add_starting(20)
obj1.add_starting(200)
obj1.add_starting(2000)
obj1.add_end(45)
obj1.add_after(58,45)
obj1.add_before(47,2000)
# obj1.delete_begin()
# obj1.delete_end()
# obj1.delete_specific_node(47)
# obj1.delete_specific_node_after(55658)
obj1.delete_specific_node_before(200)
obj1.printlinkedlist()
