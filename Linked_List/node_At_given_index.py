"""Given a singly linked list with N nodes and a number X.
The task is to find the node at the given index (X)(1 based index) of linked list.
 Ex.
 2
6 5
1 2 3 4 657 76
10 2
8 7 10 8 6 1 20 91 21 2

Output:
657
7

Explanation:
Testcase 1: Element at 5th index in the linked list is 657 (1-based indexing)."""

def getNth(head, k):
    count = 1
    while(head):
        if count == k:
            return head.data
        else:
            head = head.next
            count += 1
    return -1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

t = int(input())
for i in range(t):
    l = LinkedList()
    n, k = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    for i in reversed(a):
        l.push(int(i))
    m = getNth(l.head, k)
    print(m)
