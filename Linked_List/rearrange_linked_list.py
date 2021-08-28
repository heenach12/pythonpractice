"""Given a singly linked list, the task is to rearrange it in a way that all odd position nodes are together and all even positions node are together.
Assume the first element to be at position 1 followed by second element at position 2 and so on.

Example 1:

Input:
LinkedList: 1->2->3->4
Output: 1 3 2 4
Explanation:
Odd elements are 1, 3 and even elements are
2, 4. Hence, resultant linked list is
1->3->2->4.
Example 2:

Input:
LinkedList: 1->2->3->4->5
Output: 1 3 5 2 4
Explanation:
Odd elements are 1, 3, 5 and even elements are
2, 4. Hence, resultant linked list is
â€‹1->3->5->2->4."""

# class Solution:
def rearrangeEvenOdd(head):
    if head == None:
        return None

    odd = head
    even = head.next

    evenfirst = even

    while(1==1):
        if (odd==None or even == None or (even.next) == None):
            odd.next = evenfirst
            break

        odd.next = even.next
        odd = even.next

        if (odd.next == None):
            even.next = None
            odd.next = evenfirst
            break

        even.next = odd.next
        even = odd.next

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
    rearrangeEvenOdd(l.head)
    l.printList(l.head)
    print()
