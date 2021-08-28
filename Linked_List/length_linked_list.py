class Solution:
    def getCount(self, head_node):
        c = 1
        while head_node.next is not None:
            head_node = head_node.next
            c += 1

        return c

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = self.tail.next


t = int(input())
for i in range(t):
    n = int(input())
    a = LinkedList()
    arr = list(map(int, input().strip().split()))
    for j in arr:
        new_node = Node(j)
        a.append(new_node)
    print(Solution().getCount(a.head))

