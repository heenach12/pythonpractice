"""Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order.
Note: The flattened list will be printed using the bottom pointer instead of next pointer.



Example 1:

Input:
5 -> 10 -> 19 -> 28
|     |     |     |
7     20    22   35
|           |     |
8          50    40
|                 |
30               45
Output:  5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every
node in a single level.
(Note: | represents the bottom pointer.)
"""

#
# def merge(head1, head2):
#     if head1 == None:
#         return head2
#     elif head2 == None:
#         return head1
#     else:
#         temp = None
#         if head1.data < head2.data:
#             temp = head1
#             temp.bottom = merge(head1.bottom, head2)
#         else:
#             temp = head2
#             temp.bottom = merge(head1, head2.bottom)
#         return temp
#
#
# def flatten(head):
#     if head == None:
#         return head
#     if head.next == None:
#         return head
#
#     head.next = (flatten(head.next))
#     head = merge(head, head.next)
#
#     return head


def mergeTwoLists(node_a, node_b):
    if node_a == None:
        return node_b
    elif node_b == None:
        return node_a
    else:
        temp = None
        if node_a.data < node_b.data:
            temp = node_a
            temp.bottom = mergeTwoLists(node_a.bottom, node_b)
        else:
            temp = node_b
            temp.bottom = mergeTwoLists(node_a, node_b.bottom)
        return temp


def flatten(root):
    if root == None or root.next == None:
        return root

    root.next = flatten(root.next)

    root = mergeTwoLists(root, root.next)

    return root

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def printList(node):
    while(node):
        print(node.data, end = " ")
        node = node.bottom
    print()

t = int(input())
for i in range(t):
    head = None
    n = int(input())
    arr =[]
    arr = [int(x) for x in input().strip().split()]
    temp = None
    tempB = None
    pre = None
    preB = None

    flag = 1
    flag1 = 1

    listo = [int(x) for x in input().strip().split()]
    it = 0
    for i in range(n):
        m = arr[i]
        m -=1
        a1 = listo(it)