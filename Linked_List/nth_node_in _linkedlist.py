"""Nth node from end of linked list
Easy Accuracy: 46.6% Submissions: 100k+ Points: 2
Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from
the end of the linked list.

Example 1:

Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output: 8
Explanation: In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end os 8.
Example 2:

Input:
N = 5
LinkedList: 10->5->100->5
Output: -1
Explanation: In the second example, there
are 4 nodes in the linked list and we
need to find 5th from the end. Since 'n'
is more than the number of nodes in the
linked list, the output is -1."""

def getNthFromLast(head, n):
    temp = head
    c =0
    while temp != None:
        temp=temp.next
        c += 1
    if n>c:
        return  -1

    temp= head
    for i in range(0, c-n):
        temp= temp.next
    return temp.data


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
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = new_node

t = int(input())
for i in range(t):
    n, nth = map(int, input().strip().split())
    a = LinkedList()
    val = list(map(int, input().strip().split()))
    for i in val:
        a.append(i)
    print(getNthFromLast(a.head, nth))