class CircularQ:
    def __init__(self ,n):
        self.n = n
        self.array = [None] * self.n
        self.front = 0
        self.rear = 0
        self.size = 0

    def equeue(self, data):
        if self.size >= self.n:
            raise Exception(" Queue is full")
        self.array[self.rear] = data
        self.rear = (self.rear +1) % self.n
        self.size += 1
        return self
    
    def dequeue(self):
        if self.size == 0:
            raise Exception("Underflow Condition is detected")
        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.n
        self.size -= 1
        return temp

obj1 = CircularQ(5)
obj1.equeue(8)
obj1.equeue(28)
print(obj1.dequeue())
obj1.equeue(88)
obj1.equeue(81)
print(obj1.dequeue())
obj1.equeue(18)
print(obj1.dequeue())
obj1.equeue(187)
obj1.equeue(198)
obj1.equeue(1988)
# obj1.equeue(1988)
print(obj1.dequeue())
print(obj1.dequeue())
print(obj1.dequeue())
print(obj1.dequeue())
print(obj1.dequeue())
print(obj1.dequeue())