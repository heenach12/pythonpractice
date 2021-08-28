"""Given a linked list of size N. The task is to complete the function countNodesinLoop() that checks whether a given Linked List contains a loop or not and if the loop is present then return the count of nodes in a loop or else return 0. C is the position of the node to which the last node is connected. If it is 0 then no loop.
Input:
N = 10
value[]={25,14,19,33,10,21,39,90,58,45}
C = 4
Output: 7
Explanation: The loop is 45->33. So
length of loop is 33->10->21->39->
90->58->45 = 7. The number 33 is
connected to the last node to form the
loop because according to the input the
4th node from the beginning(1 based
index) will be connected to the last
node for the loop.

"""

class Solution:
    def length_loop(self, head):
        if self.head == None:
            return 0

        slow = head
        fast = head
        flag = 0

        while(slow and slow.next and fast and fast.next and fast.next.next):
            if (slow == fast and flag != 0):
                c = 1
                slow = slow.next
                while (slow != fast):
                    slow = slow.next
                    c += 1
                return c

        slow = slow.next
        fast = fast.next.next
        flag = 1
        return 0