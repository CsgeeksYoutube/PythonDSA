#implemeting Queue With list

# queue1 = []
# queue1.append(10)
# queue1.append(20)
# queue1.append(30)

# print(queue1)
# # print(queue.pop(0))
# # print(queue.pop(0))
# # print(queue.pop(0))
# queue = []
# queue.insert(0,10)
# queue.insert(0,20)
# queue.insert(0,30)
# print(queue)
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())

#  implemeting queue with collection.dequeue
# import collections
# q = collections.deque()
# q.append(20)
# q.append(10)
# q.append(30)
# q.append(50)
# q.appendleft(10)
# q.appendleft(20)
# q.appendleft(30)
# q.appendleft(40)
# print(q)
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())

# q= []
# q.append(10)
# q.append(120)
# q.append(300)
# q.append(80)
# q.sort()
# print(q)
# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))

import queue
q = queue.PriorityQueue()
q.put(10)
q.put(130)
q.put(60)
q.put(900)
print(q.get())
print(q.get())
print(q.get())
print(q.get())