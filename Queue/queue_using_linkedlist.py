class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.rear = self.front = None

    def isEmpty(self):
        return self.front == None

    def enQueue(self, data):
        temp = Node(data)
        if self.rear == None:
            self.rear = self.front = temp
            return
        else:
            self.rear.next = temp
            self.rear = temp

    def deQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return temp.data


q = Queue()
q.enQueue(2)
q.enQueue(4)
q.enQueue(6)
print(q.front.data)
print(q.rear.data)

q.deQueue()
q.enQueue(9)
print(q.front.data)
print(q.rear.data)
