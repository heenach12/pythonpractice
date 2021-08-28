class Solution:
    def display(self, node):
        while(node):
            print(node.data, end = " ")
            node = node.next

class Node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node()
            self.head.data = data
        else:
            new_node = Node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node

t = int(input())
for i in range(t):
    llist = LinkedList()
    n = int(input())
    values = list(map(int, input().strip().split()))
    for i in values:
        llist.insert(i)
    Solution().display(llist.get_head())
    print("")