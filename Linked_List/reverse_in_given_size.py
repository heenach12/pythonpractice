"""Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.

Example 1:

Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5
Explanation:
The first 4 elements 1,2,2,4 are reversed first
and then the next 4 elements 5,6,7,8. Hence, the
resultant linked list is 4->2->2->1->8->7->6->5.
Example 2:

Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4
Explanation:
The first 3 elements are 1,2,3 are reversed
first and then elements 4,5 are reversed.Hence,
the resultant linked list is 3->2->1->5->4"""

class Solution:
    def reverseSize(self, head, k):
        """ Iterative approach"""
        # prev = None
        # curr = head
        # join = None
        # temp = None
        # new_head = None
        # t = 0
        # tail = None
        #
        # while(curr):
        #     t = k
        #     join = curr
        #     prev = None
        #
        #     while(curr and t >0):
        #         temp = curr.next
        #         curr.next = prev
        #         prev= curr
        #         curr = temp
        #         t -= 1
        #
        #     if new_head == None:
        #         new_head = prev
        #
        #     if tail != None:
        #         tail.next = prev
        #
        #     tail = join
        # return new_head

        """Recursive Approach"""
        prev = None
        curr = head
        temp = None

        c = 0
        while(curr and c < k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            c += 1

        if temp is not None:
            head.next = self.reverseSize(temp, k)

        return prev

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
    k = int(input())
    ob = Solution().reverseSize(lis.head, k)
    printList(ob)
