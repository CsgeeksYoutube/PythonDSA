class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            i = 1
            while True:
                new_index = (index + i ** 2) % self.size
                if self.table[new_index] is None:
                    self.table[new_index] = (key, value)
                    break
                i += 1
                if i == self.size:
                    print("Hash table is full.")
                    break

    def display(self):
        print("Hash Table:")
        for i, item in enumerate(self.table):
            print(i, ":", item)



hash_table = HashTable(10)
hash_table.insert(5, 'A')
hash_table.insert(15, 'B')
hash_table.insert(25, 'C')
hash_table.insert(35, 'D')
hash_table.insert(45, 'E')
hash_table.insert(55, 'F')
hash_table.display()
