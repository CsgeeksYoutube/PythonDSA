class DoubleHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash1(self, key):
        return hash(key) % self.size

    def hash2(self, key):
        return 1 + (hash(key) % (self.size - 1))

    def insert(self, key, value):
        index = self.hash1(key)
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
        else:
            step = self.hash2(key)
            while self.keys[index] is not None:
                index = (index + step) % self.size
            self.keys[index] = key
            self.values[index] = value

    def search(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + step) % self.size
        return None

    def delete(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = (index + step) % self.size

    def print_hashtable(self):
        print("Hashtable Contents:")
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f"Index {i}: Key: {self.keys[i]}, Value: {self.values[i]}")
            else:
                print(f"Index {i}: Empty")

hash_table = DoubleHashTable(10)  

hash_table.insert("apple", 5) 
hash_table.insert("banana", 10)  
hash_table.insert("orange", 7) 
hash_table.insert("cake", 5) 
hash_table.insert("bun", 10)  
hash_table.insert("org", 7)  
hash_table.insert("app", 5) 
hash_table.insert("bana", 10)  
hash_table.insert("ora", 7)  
hash_table.insert("appltetete", 5) 
hash_table.print_hashtable()

result = hash_table.search("apple")
if result is not None:
    print("Value found for 'apple':", result)
else:
    print("Value not found for 'apple'")

hash_table.delete("banana")
result = hash_table.search("bun")
if result is not None:
    print("Value found for 'banana':", result)
else:
    print("Value not found for 'banana'")
