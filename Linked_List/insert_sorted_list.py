"""Given a sorted singly linked list and a data, your task is to insert the data in the linked list in a sorted way i.e. order of the list doesn't change.

Example 1:

Input:
LinkedList: 25->36->47->58->69->80
data: 19
Output: 19 25 36 47 58 69 80
Example 2:

Input:
LinkedList: 50->100
data: 75
Output: 50 75 100"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __int__(self):
        self.head = None
        self.prev= self.head

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.prev = self.head
        else:
            self.prev.next = new_node
            self.prev = self.prev.next

def printList(head):
    while (head):
        print(head.data, end = " ")
        head = head.next
    print( )

class Solution:
    def sortedInsert(self, head1, key):
        newnode = Node(key)
        if head is None:
            head = newnode
            return head
        if head.data >= key:
            newnode.next = head
            head = newnode
            return head
        flag = head
        d = 0
        while flag.next is not None:
            if flag.next.data >= key:
                newnode.next = flag.next
                flag.next = newnode
                d = 1
                break
            flag = flag.next
        if d == 0:
            flag.next = newnode
        return head

        # node = Node(key)
        #
        # if head1 is None:
        #     node.next = head1
        #     head1 = node
        # elif head1.data >= node.data:
        #     node.next = head1
        #     head1 = node
        # else:
        #     curr = head1
        #     while(curr.next is not None and curr.next.data < node.data):
        #         curr = curr.next
        #     node.next = curr.next
        #     curr.next = node
        # return head1

n = int(input())
a  = LinkedList()
nodes = list(map(int, input().strip().split()))
for x in nodes:
    a.append(x)
key = int(input())
h = Solution().sortedInsert(a.head, key)
printList(h)
