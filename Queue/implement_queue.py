"""Implement Queue using list"""

q = []
q.append(1)
q.append(2)
q.append(3)

q.pop(0)
q.pop(0)
q.pop(0)

"""Implmenet Queue using deque"""

from collections import deque
q = deque()
q.append(2)
q.append(3)
q.append(7)

q.popleft()
q.popleft()
q.popleft()


"""Implement Queue using Queue.Queue"""
from queue import  Queue
a = Queue(maxsize=4)
print(a.qsize())

a.empty()
a.full()

a.put(3)
a.put(8)
a.put(10)

a.get()
a.get()
a.get()
