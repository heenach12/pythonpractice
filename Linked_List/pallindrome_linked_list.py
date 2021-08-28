"""Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.

Example 1:

Input:
N = 3
value[] = {1,2,1}
Output: 1
Explanation: The given linked list is
1 2 1 , which is a palindrome and
Hence, the output is 1.
Example 2:

Input:
N = 4
value[] = {1,2,3,4}
Output: 0
Explanation: The given linked list
is 1 2 3 4 , which is not a palindrome
and Hence, the output is 0."""

class Solution:
    def reverse(self, head):
        curr = head
        prev = None
        next = None

        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def compareLists(self, head1, head2):
        temp1 = head1
        temp2 = head2

        while(temp1 and temp2):
            if temp1.data == temp2.data:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return 0

        if (temp1 == None and temp2 == None):
            return 1
        return 0

    def isPalindrome(self, head):
        """Stack approach"""
        # temp = head
        #
        # ispalin = True
        # st =[]
        #
        # while(temp is not None):
        #     st.append(temp.data)
        #     temp = temp.next
        #
        # while ( head != None):
        #     i = st.pop()
        #     if head.data == i:
        #         ispalin = True
        #     else:
        #         ispalin = False
        #         break
        #     head = head.next
        #
        # return ispalin


        """Iterative approach"""
        fast = head
        slow = head
        prev_slow = head
        mid = None

        res = True

        if (head != None and head.next != None):
            while(fast != None and fast.next != None):
                fast = fast.next.next
                prev_slow = slow
                slow = slow.next

            if fast != None:
                mid = slow
                slow = slow.next

            second_half = slow
            prev_slow.next = None

            second_half = self.reverse(second_half)

            res = self.compareLists(head, second_half)

            second_half = self.reverse(second_half)

            if (mid  != None):
                prev_slow.next = mid
                mid.next = second_half
            else:
                prev_slow = second_half

        return res

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while(n):
        print(n.data, end = " ")
        n = n.next
    print(" ")

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = LinkedList()
    for i in arr:
        lis.insert(i)
    # k = int(input())
    # ob = Solution().ispallindrome(lis.head, k)
    if Solution().isPalindrome(lis.head):
        print(1)
    else:
        print(0)