class Node:
    def __init__(self,data):
        self.pref = None
        self.data = data
        self.nref = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_starting(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref =self.head
            self.head.pref = new_node
            self.head = new_node

    def printdoublylinkedlist(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp= self.head
            while temp is not None:
                print(temp.data)
                temp = temp.nref

    def printdoublylinkedlistreverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp= self.head
            while temp is not None:
                ptr = temp
                temp = temp.nref
            print("linked list in reverse order")
            while ptr is not None:
                print(ptr.data)
                ptr = ptr.pref

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.nref is not None:
                temp = temp.nref
            temp.nref = new_node
            new_node.pref = temp

    def add_after(self,data,value):
        if self.head is None:
            print("linked list is empty")
            return
        
        temp = self.head
        while(temp.data != value):
            temp = temp.nref
            if temp is None:
                print("Node is not found")
                return

        new_node = Node(data)
        new_node.pref = temp
        new_node.nref = temp.nref
        temp.nref = new_node
        if new_node.nref is not None:
            new_node.nref.pref = temp.nref

    def add_before(self,data,value):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.data == value:
            new_node = Node(data)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            return
        temp = self.head
        while(temp.data != value):
            ptr = temp
            temp = temp.nref
            if temp is None:
                print("node is not found")
                return
        new_node = Node(data)
        new_node.nref = temp
        new_node.pref = ptr
        ptr.nref = new_node
        temp.pref = new_node
            
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty")
            return
        else:
            temp = self.head
            self.head = temp.nref
            if temp.nref is not None:
                self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
            return
        elif self.head.nref is None:
            self.head = None
        else:
            temp = self.head
            ptr = temp.nref
            while ptr.nref is not None:
                temp = temp.nref
                ptr = ptr.nref
            temp.nref = None
            ptr = None
    
    def delete_specific_node(self, x):
        if self.head is None:
            print("linked list is empty")
            return
        if x == self.head.data:
            self.head = self.head.nref
            if self.head is not None:
                self.head.pref = None
            return
        temp = self.head
        while(temp.data != x):
            ptr = temp
            temp = temp.nref
            if temp is None:
                print("node is not found")
                return
        ptr.nref = temp.nref
        if temp.nref is None:
            return
        ptr.nref.pref = ptr

    def delete_specific_node_after(self,x):
        if self.head is None:
            print("linked list is empty")
            return
        temp = self.head
        while temp.data != x:
            temp= temp.nref
            if(temp is None):
                print("node is not found")
                return
        if temp.nref is None:
            print("node is not found")
            return
        elif (temp.nref.nref is None):
            ptr = temp.nref
            temp.nref = ptr.nref
            ptr = None
        else:
            ptr = temp.nref
            temp.nref = ptr.nref
            ptr.nref.pref = temp
    
    def delete_specific_node_before(self, x):
        if self.head is None:
            print("linked list is empty")
            return
        temp = self.head
        ptr = temp.nref
        if(ptr is None or temp.data == x):
            print("cant be deleted")
            return
        if (ptr.data == x):
            self.head = self.head.nref
            self.head.pref = None
            return
        if(ptr.nref is None):
            print("node does not exist")
            return        
        while( ptr.nref.data !=x):
            ptr = ptr.nref
            temp= temp.nref
            if (ptr.nref is None):
                print("node does not exist")
                return 
        temp.nref = ptr.nref
        ptr.nref.pref = temp
        ptr = None




obj1 = DoublyLinkedList()
obj1.add_starting(20)
obj1.add_starting(200)
obj1.add_starting(2000)
obj1.add_after(120,200)
obj1.add_before(459,20)
# obj1.delete_begin()
# obj1.delete_end()
# obj1.delete_specific_node(200)
# obj1.delete_specific_node_after(120)
obj1.delete_specific_node_before(200)
obj1.printdoublylinkedlist()
obj1.printdoublylinkedlistreverse()