"""Your task is to implement  2 stacks in one array efficiently.



Example 1:

Input:
push1(2)
push1(3)
push2(4)
pop1()
pop2()
pop2()

Output:
3 4 -1

Explanation:
push1(2) the stack1 will be {2}
push1(3) the stack1 will be {2,3}
push2(4) the stack2 will be {4}
pop1()   the poped element will be 3
from stack1 and stack1 will be {2}
pop2()   the poped element will be 4
from stack2 and now stack2 is empty
pop2()   the stack2 is now empty hence -1 ."""

class twoStack:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 < self.top2-1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
        else:
            print("Stack overflow")
            return False

    def push2(self, x):
        if self.top1 < self.top2 -1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
        else:
            print("stack overflow")
            return False

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= self.top1
            return x
        else:
            print("stack overflow")
            return False

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += self.top2
            return x
        else:
            print("stack overflow")
            return False


ts = twoStack(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
ts.pop1()
ts.push2(40)
ts.pop2()
print(ts.arr)
