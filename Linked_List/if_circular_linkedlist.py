"""Given a singly linked list, find if the linked list is circular or not. A linked list is called circular if it not NULL terminated and all nodes are connected in the form of a cycle. An empty linked list is considered as circular.

Example 1:

Input:
LinkedList: 1->2->3->4->5
(the first and last node is connected,
i.e. 5 --> 1)
Output: 1
Example 2:

Input:
LinkedList: 2->4->6->7->5->1
Output: 0"""

def isCircular(head):
    temp = head
    if head is None:
        return True

    while(temp.next != head):
        temp = temp.next
        if temp == None:
            break

    if temp == None:
        return False
    else:
        return True