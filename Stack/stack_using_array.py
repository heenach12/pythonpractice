class Stack:
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if len(self.arr) >=1:
            return self.arr.pop()
        return -1

t = int(input())
for i in range(t):
    n = int(input())
    s = Stack()
    a = list(map(int, input().strip().split()))
    i = 0
    while(i< len(a)):
        if a[i] == 1:
            s.push(a[i+1])
            i+= 2
        elif a[i] == 2:
            print(s.pop(), end = " ")
            i += 1
        