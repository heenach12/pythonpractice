class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.stktop = None

    def push(self, x):
        self.q1.append(x)
        self.stktop = x


    def pop(self):

        while len(self.q1) > 1:
            self.stktop = self.q1.pop(0)
            self.q2.append(self.stktop)

        res = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self):
        return self.stktop

    def isEmpty(self):
        return len(self.q1) == 0


q = Stack()
q.push(1)
q.push(5)
q.push(3)
print(q.pop())
q.push(2)
print(q.pop())

