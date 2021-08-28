"""Delete xth node from a singly linked list. Your task is to complete the method deleteNode() which takes two arguments: the address of the head of the linked list and an integer x. The function returns the head of the modified linked list.

Input:
The first line of input contains an element T, denoting the number of test cases. Then T test cases follow. Each test case contains three lines. The first line of each test case contains an integer N denoting the number of elements of the linked list. Then in the next line are N space separated values of the linked list. The third line of each test case contains an integer x.

Output:
The output for each test case will be the space separated value of the returned linked list.

User Task:
The task is to complete the function deleteNode() which should delete the node at required position.

Constraints:
1 <= T <= 300
2 <= N <= 100
1 <= x <= N

Example:
Input:
2
3
1 3 4
3
4
1 5 2 9
2

Output:
1 3
1 2 9

Explanation:
Testcase 1: After deleting the node at 3rd position (1-base indexing), the linked list is as 1-> 3.
Testcase 2: After deleting the node at 2nd position (1-based indexing), the linked list is as 1-> 2-> 9."""
def delNode(head, k):
    # import pdb; pdb.set_trace()
    cur=head
    if k == 1:
        return cur.next
    k -= 1
    while k > 1:
        cur = cur.next
        k -= 1
    cur.next = cur.next.next
    return head

    # temp = head
    #
    # while(temp is not None):
    #     if temp.data == k:
    #         head = temp.next
    #         temp = None
    #         return
    #
    # while(temp is not None):
    #     if temp.data == k:
    #         break
    #     prev = temp
    #     temp = temp.next
    #
    # if temp == None:
    #     return
    #
    # prev.next = temp.next
    # temp=None
    #
    # return head
    #

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

    new_head= delNode(a.head, k)
    print_list(new_head)