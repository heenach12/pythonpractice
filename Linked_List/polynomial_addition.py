class Node:
    def __init__(self, coeff, pwr):
        self.coeff = coeff
        self.next = None
        self.pwr = pwr

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, coeff, pwr):
        if self.head == None:
            self.head = Node(coeff, pwr)
            return
        else:
            new_node = Node(coeff, pwr)
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node

def createList(arr, n):
    l = LinkedList()
    k = 0
    for i in range(n):
        l.insert(arr[k], arr[k+1])
        k += 2
    return l.head

class Solution:
    def polynomialAddition(self, poly1, poly2):
        head = Node(0,0)
        t =  head
        while(poly1 != None and poly2 != None):
            if poly1.pwr == poly2.pwr:
                t.next = Node(poly1.coeff+poly2.coeff, poly1.pwr)
                poly1 = poly1.next
                poly2 = poly2.next
            elif (poly1.pwr > poly2.pwr):
                t.next = Node(poly1.coeff, poly1.pwr)
                poly1 = poly1.next
            else:
                t.next = Node(poly2.coeff, poly2.pwr)
                poly2 = poly2.next
            t = t.next
        while(poly1 != None):
            t.next = poly1
            t = t.next
            poly1 = poly1.next

        while (poly2 != None):
            t.next = poly2
            t = t.next
            poly2 = poly2.next
        return head.next

        # p = poly1
        # q = poly2
        # ptr = Node()
        # poly = ptr
        #
        # while(p.next and q.next):
        #     if (p.pwr > q.pwr):
        #         ptr.coeff = p.coeff
        #         ptr.pwr = p.pwr
        #         p = p.next
        #     elif (p.pwr < q.pwr):
        #         ptr.coeff = q.coeff
        #         ptr.pwr = q.pwr
        #         q = q.next
        #     else:
        #         ptr.coeff = p.coeff + q.coeff
        #         ptr.pwr = p.pwr
        #         p = p.next
        #         q = q.next
        #     ptr.next = Node()
        #     ptr = ptr.next
        # if (p.next):
        #     ptrr = p
        # if (q.next):
        #     ptrr = q
        # while(ptrr.next):
        #     ptr.coeff = ptrr.coeff
        #     ptr.pwr = ptrr.pwr
        #     ptr.next = Node()
        #     ptr = ptr.next
        #     ptrr = ptrr.next
        # ptr.next = None
        # return ptr


t = int(input())
for i in range(t):
    n = int(input())
    a1 = list(map(int, input().strip().split()))
    poly1 = createList(a1, n)
    n = int(input())
    a2 = list(map(int, input().strip().split()))
    poly2 = createList(a2, n)
    s = Solution().polynomialAddition(poly1, poly2)
    ptr = s
    while ptr is not None:
        print(str(ptr.coeff) + "x^" + str(ptr.pwr), end = " ")
        ptr = ptr.next
        if ptr is not None:
            print(" +", end=" ")
    print()