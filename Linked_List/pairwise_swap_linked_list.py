"""Given a singly linked list of size N. The task is to swap elements in the linked list pairwise.
For example, if the input list is 1 2 3 4, the resulting list after swaps will be 2 1 4 3.
Note: You need to swap the nodes, not only the data. If only data is swapped then driver will print -1.

Example 1:

Input:
LinkedList: 1->2->2->4->5->6->7->8
Output: 2 1 4 2 6 5 8 7
Explanation: After swapping each pair
considering (1,2), (2, 4), (5, 6).. so
on as pairs, we get 2, 1, 4, 2, 6, 5,
8, 7 as a new linked list."""

class Solution:
    def pairWiseSwap(self, head):
        if head.next is None and head:
            return head

        p = head
        new_head = p.next

        while(p):
            q = p.next
            temp = q.next
            q.next = p
            if temp == None or temp.next == None:
                p.next = temp
                break
            p.next = temp.next
            p = temp
        return new_head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while(n):
        print(n.data, end = " ")
        n = n.next
    print(" ")

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = LinkedList()
    for i in arr:
        lis.insert(i)

    dict1 = {}
    temp = lis.head
    while(temp):
        dict1[temp] = temp.data
        temp = temp.next

    failure = LinkedList()
    failure.insert(-1)

    head = Solution().pairWiseSwap(lis.head)

    temp = head
    f = 0
    while(temp):
        if dict1[temp] != temp.data:
            f = 1
        temp = temp.next

    if f:
        printList(failure)
    else:
        printList(head)
