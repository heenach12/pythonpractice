"""Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
Note: Try not to use extra space. Expected time complexity is O(N). The nodes are arranged in a sorted way.

Example 1:

Input:
LinkedList: 2->2->4->5
Output: 2 4 5
Explanation: In the given linked list
2 ->2 -> 4-> 5, only 2 occurs more
than 1 time.
Example 2:

Input:
LinkedList: 2->2->2->2->2
Output: 2
Explanation: In the given linked list
2 ->2 ->2 ->2 ->2, 2 is the only element
and is repeated 5 times.
"""


class Solution:
    def removeDuplicates(self, head):
        if head == None or head.next == None:
            return head

        temp = head
        s = set()
        s.add(temp.data)

        while(temp.next is not None):
            if temp.next.data in s:
                temp.next = temp.next.next
            else:
                s.add(temp.next.data)
                temp = temp.next
        return head

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

    def printList(self):
        if self.head is None:
            print(" ")
            return
        curr = self.head
        while (curr):
            print(curr.data, end=" ")
            curr = curr.next
        print(" ")


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = LinkedList()
    for i in arr:
        lis.insert(i)

    newhead = Solution().removeDuplicates(lis.head)
    lis.printList()