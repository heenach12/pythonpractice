"""Given a link list of size N, modify the list such that all the even numbers appear before all the odd numbers in the modified list. The order of appearance of numbers within each segregation should be same as that in the original list.


Example 1:

Input:
N = 7
Link List =
17 -> 15 -> 8 -> 9 -> 2 -> 4 -> 6 -> NULL

Output: 8 2 4 6 17 15 9

Explaination: 17,15,8,9 are odd so they appear
first and 2,4,6 are the even numbers that appear later.

Example 2:

Input:
N = 4
Link List = 1 -> 3 -> 5 -> 7

Output: 1 3 5 7

Explaination: There is no even number.
So ne need for modification.
"""
class Solution:
    def divide(self, n, head):
        odd_l = []
        even_l = []

        temp = head
        while(temp is not None):
            if (temp.data) % 2 == 0:
                even_l.append(temp)
                prev = temp
                temp = temp.next
                prev.next = None
            else:
                odd_l.append(temp)
                prev = temp
                temp = temp.next
                prev.next = None

        if len(even_l) > 0:
            head = even_l.pop(0)
            t = head

        while(len(even_l)> 0):
            x = even_l.pop(0)
            t.next = x
            t = t.next
        if t is None:
            x = odd_l.pop(0)
            t = x
        while(len(odd_l) > 0):
            x = odd_l.pop(0)
            t.next = x
            t = t.next
        return head


        # oddstart =None
        # oddend = None
        #
        # evenstart = None
        # evenend = None
        #
        # temp = head
        #
        # while(temp != None):
        #     val = temp.data
        #     if (val %2 == 0):
        #         if (evenstart == None):
        #             evenstart = temp
        #             evenend = evenstart
        #         else:
        #             evenend.next = temp
        #             evenend = evenend.next
        #     else:
        #         if(oddstart == None):
        #             oddstart = temp
        #             oddend = oddstart
        #         else:
        #             oddend.next = temp
        #             oddend = oddend.next
        #     temp = temp.next
        #
        # if ((oddstart == None) or (evenstart == None)):
        #     return head
        #
        # # if evenend == None:
        # evenend.next = oddstart
        # oddend.end = None
        #
        # head = evenstart
        #
        # return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
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
    while(temp is not None):
        print(temp.data, end=" ")
        temp= temp.next
    print(" ")

t = int(input())
for i in range(t):
    l1 = LinkedList()
    n = int(input())
    val = list(map(int, input().strip().split()))
    for i in val:
        l1.insert(i)
    ob = Solution()
    newhead = ob.divide(n, l1.head)
    print_list(newhead)