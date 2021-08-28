""""First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the linked list and next M and N respectively space separated. The last line contains the elements of the linked list.

Output:
Function should not print any output to stdin/console.

User Task:
The task is to complete the function linkdelete() which should modify the linked list as required.

Example:
Input:
2
8
2 1
9 1 3 5 9 4 10 1
6
6 1
1 2 3 4 5 6

Output:
9 1 5 9 10 1
1 2 3 4 5 6

Explanation:
Testcase 1: Deleting one node after skipping the M nodes each time, we have list as 9-> 1-> 5-> 9-> 10-> 1.
 """


def skipMdeleteN(head, m, n):
    temp = head
    while(temp):
        for count in range(1, m):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        t = temp.next
        for count in range(1, n+1):
            if t is None:
                return
            t = t.next

        temp.next = t
        temp = t
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
    k = int(input())
    a = LinkedList()
    val = list(map(int, input().strip().split()))
    for i in val:
        a.append(i)
    m = int(input())
    n = int(input())
    new_head= skipMdeleteN(a.head, m, n)
    print_list(new_head)