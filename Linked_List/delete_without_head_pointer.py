"""You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. The task is to delete the node. Pointer/ reference to head node is not given.
Note: No head reference is given to you. It is guaranteed that the node to be deleted is not a tail node in the linked list.

Example 1:

Input:
N = 2
value[] = {1,2}
node = 1
Output: 2
Explanation: After deleting 1 from the
linked list, we have remaining nodes
as 2.
Example 2:

Input:
N = 4
value[] = {10,20,4,30}
node = 20
Output: 10 4 30
Explanation: After deleting 20 from
the linked list, we have remaining
nodes as 10, 4 and 30."""

class Solution:
    def deleteNode(self, node):
        temp = node
        temp.data = temp.next.data
        temp.next = temp.next.next
        return temp


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def getNode(self, value):
        temp = self.head
        while(temp.next and temp.data != value):
            temp = temp.next
        if (temp.data == value):
            return temp
        else:
            return None

    def printList(self):
        if self.head is None:
            print(" ")
            return
        temp = self.head
        while(temp):
            print(temp.data, end= " ")
            temp = temp.next
        print(" ")


t = int(input())
for i in range(t):
    n = int(input())
    a = LinkedList()
    val = list(map(int, input().strip().split()))
    for j in val:
        a.append(j)

    del_el = int(input())
    to_delete = a.getNode(del_el)
    Solution().deleteNode(to_delete)
    a.printList()

