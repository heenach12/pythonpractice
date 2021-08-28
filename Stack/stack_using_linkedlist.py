class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while(cur):
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def peek(self):
        if self.isEmpty():
            raise Exception("Popping from empty stack")
        return self.head.next.value

    def push(self, v):
        node = Node(v)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from empty stack")
        r = self.head.next
        self.head.next = self.head.next.next
        self.size -=1
        return r.value


t = int(input())
for i in range(t):
    n = int(input())
    s = Stack()
    a = list(map(int, input().strip().split()))
    i = 0
    while (i < len(a)):
        if a[i] == 1:
            s.push(a[i + 1])
            i += 2
        elif a[i] == 2:
            print(s.pop(), end=" ")
            i += 1
