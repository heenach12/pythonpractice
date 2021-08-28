"""Given a singly linked list, your task is to remove every kth node from the linked list.

Input:
The first line of input contains number of test cases T. Then T test cases follow.
Every test case contains 3 lines. First line of every test case contains an integer N denoting the
 size of the linked list . The second line contains N space separated values of the linked list.
 The third line contains an integer K.

Output:
Output for each test case will be space separated values of the nodes of the new transformed linked list.

User Task:
The task is to complete the function deleteK() which should delete every kth nodes from the linked list.

Constraints:
1 <= T <= 50
1 <= N <= 100
1 <= element of linked list <= 1000
0 <= k <= 100

Example:
Input:
2
8
1 2 3 4 5 6 7 8
3
4
1 2 3 4
2

Output:
1 2 4 5 7 8
1 3

Explanation:
Testcase 1: After removing every 3rd element from the linked list, we have updated list as 1, 2, 4, 5, 7 and 8,
 and the elements which are removed are 3 and 6."""
def freeList(node):
    while(node!=None):
        node.next = None
        node= None
    return node

def deleteK(head, k):
    if head == None:
        return None

    if k == 1:
        freeList(head)
        return None

    temp =head
    prev = None

    c = 0
    while(temp!=None):
        c += 1
        if (k == c):
            prev.next = temp.next
            c = 0

        if c != 0:
            prev = temp

        temp = prev.next

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

def print_list(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp= temp.next
    print(" ")



t = int(input())
for i in range(t):
    n = int(input())
    a = LinkedList()
    val = list(map(int, input().strip().split()))
    for i in val:
        a.append(i)
    k = int(input())

    new_head= deleteK(a.head, k)
    print_list(new_head)