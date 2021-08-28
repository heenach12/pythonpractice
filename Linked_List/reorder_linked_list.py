"""Given a singly linked list: A0→A1→…→An-1→An, reorder it to: A0→An→A1→An-1→A2→An-2→…
For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

Note: It is recommended do this in-place without altering the nodes' values.

Example 1:

Input:
LinkedList: 1->2->3
Output: 1 3 2
Example 2:

Input:
LinkedList: 1->7->3->4
Output: 1 4 7 3."""
def reorder_list(head):
    if head == None or head.next == None:
        return

    slow = head
    fast = head

    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow

    while(curr):
        t = curr.next
        curr.next = prev
        prev= curr
        curr = t

    n1 = head
    n2 = prev

    while(n2.next != None):
        t = n1.next
        n1.next = n2
        n1 = t

        t =n2.next
        n2.next = n1
        n2 = t

    return head


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

    def newNode(self, key):
        temp = Node(key)
        self.next =None
        return temp

    def printList(self, node):
        while(node):
            print(node.data, end= " ")
            node = node.next

    # def push(self, new_data):
    #     new_node = Node(new_data)
    #     new_node.next = self.head
    #     self.head = new_node


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    l = LinkedList()
    for j in a:
        l.append(j)
    # Solution().rearrangeEvenOdd(l.head)
    # Solution().rearrangeEvenOdd(l.head)
    reorder_list(l.head)
    l.printList(l.head)
    print()
