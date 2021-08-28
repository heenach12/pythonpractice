"""Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

Example 1:

Input:
N = 3
value[] = {1,3,4}
x = 2
Output: True
Explanation: In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop."""

class Solution:
    def startloop(self, p, head):
        q = head

        while(p!=q):
            p = p.next
            q = q.next

        return p

    def detectloop(self, head):
        p = head
        q = head
        while(p and q and q.next):
            p = p.next
            q= q.next.next

            if (p == q):
                k = self.startloop(p, head)
                print("k is", k)
                return True
        return False


def createloop(self, x):
    if x == 0:
        return

    t = self.head
    for i in range(1, x):
        t = t.next

    self.tail.next = t

