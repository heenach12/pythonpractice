"""Given a linked list of N nodes. The task is to reverse this list.

Example 1:

Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list,
elements are 6->5->4->3->2->1.
Example 2:

Input:
LinkedList: 2->7->8->9->10
Output: 10 9 8 7 2
Explanation: After reversing the list,
elements are 10->9->8->7->2."""

class Solution:
    def reverseList(self, head):
        """Below is the stack approach"""
        stack = []
        temp = head

        while(temp):
            stack.append(temp)
            temp = temp.next

        head = temp = stack.pop()

        elem = None
        while(len(stack)> 0):
            elem = stack.pop()
            temp.next = elem
            temp = elem

        elem.next = None
        return head

        """Below is Iterative approach"""
        # next = None
        # prev = None
        # curr = head
        #
        # while(curr is not None):
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # head = prev
        #
        # return head

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

    newhead = Solution().reverseList(lis.head)
    printList(newhead)