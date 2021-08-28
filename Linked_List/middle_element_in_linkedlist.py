"""Given a singly linked list of N nodes. The task is to find the middle of the linked list. For example, if given linked list is 1->2->3->4->5 then the output should be 3.
If there are even nodes, then there would be two middle nodes, we need to print the second middle element. For example, if given linked list is 1->2->3->4->5->6 then the output should be 4.

Example 1:

Input:
LinkedList: 1->2->3->4->5
Output: 3
Explanation:
Middle of linked list is 3.
Example 2:

Input:
LinkedList: 2->4->6->7->5->1
Output: 7
Explanation:
Middle of linked list is 7."""

def findMid(head):
    slow = head
    fast = head

    # Iterate till fast's next is null (fast reaches end)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data
    # return res

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = self.tail.next

def createList(arr, n):
    lis = LinkedList()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    head = createList(arr, n)
    print(findMid(head))
