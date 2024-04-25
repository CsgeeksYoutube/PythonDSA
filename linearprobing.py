class LinearProbeHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def _probe(self, key, index):
        return (index + 1) % self.size

    def put(self, key, value):
        index = self._hash(key)
        while self.keys[index] is not None:
            print("collision occur")
            if self.keys[index] == key:
                self.values[index] = value
                print ("same index may be different value")
                return
            index = self._probe(key, index)
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._probe(key, index)
        return None
hash_table = LinearProbeHashTable(10)
hash_table.put(123, "apple")
hash_table.put(123, "orange")
hash_table.put(453, "banana")
hash_table.put(789, "grape")

print("Value of key 123:", hash_table.get(453))