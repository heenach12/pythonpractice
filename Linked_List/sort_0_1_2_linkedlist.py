"""Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.

Example 1:

Input:
N = 8
value[] = {1,2,2,1,2,0,2,2}
Output: 0 1 1 2 2 2 2 2
Explanation: All the 0s are segregated
to the left end of the linked list,
2s to the right end of the list, and
1s in between.
Example 2:

Input:
N = 4
value[] = {2,2,0,1}
Output: 0 1 2 2
Explanation: After arranging all the
0s,1s and 2s in the given format,
the output will be 0 1 2 2."""

class Solution:
    def sortedLinked(self, head):
        temp = head
        count = [0, 0, 0]

        while(temp):
            count[temp.data] += 1
            temp = temp.next

        i = 0
        temp = head
        while(temp):
            if count[i] == 0:
                i += 1
            else:
                temp.data = i
                count[i] -= 1
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

    newhead = Solution().sortedLinked(lis.head)
    lis.printList()