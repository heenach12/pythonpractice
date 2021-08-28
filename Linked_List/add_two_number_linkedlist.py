class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_ll(head):
    if head is None:
        return None

    if head.next is None:
        return head

    p = None
    c = head
    n = None
    while (c is not None):
        n =  c.next
        c.next = p
        p = c
        c = n
    return p

def addLists(first, second):
    carry = 0
    f_r =  reverse_ll(first)
    s_r = reverse_ll(second)

    p3 = None
    sum_p = None

    while ( f_r is not None and s_r is not None):
        s = f_r.data + s_r.data + carry
        if s//10 > 0:
            carry = s//10
            s = s%10
        else:
            carry = 0

        if p3 is None:
            p3 = Node(s)
            sum_p = p3
        else:
            new_node = Node(s)
            p3.next = new_node
            p3 = new_node

        f_r = f_r.next
        s_r= s_r.next


    while(f_r is not None):
        s = f_r.data + carry
        if s//10 > 0:
            carry = s//10
            s = s % 10
        else:
            carry = 0

        if p3 is None:
            p3 = Node(s)
            sum_p = p3
        else:
            new_node = Node(s)
            p3.next = new_node
            p3 = new_node
        f_r = f_r.next

    while(s_r is not None):
        s = s_r.data + carry
        if s//10 > 0:
            carry = s//10
            s = s % 10
        else:
            carry = 0

        if p3 is None:
            p3 = Node(s)
            sum_p = p3
        else:
            new_node = Node(s)
            p3.next = new_node
            p3 = new_node
        s_r = s_r.next

    if carry != 0:
        new_node = Node(carry)
        p3.next = new_node
        p3 = new_node

    return reverse_ll(sum_p)


    # code here
    # return head of sum list
    # carry = 0
    # pointer_1 = reverse_ll(first)
    # pointer_2 = reverse_ll(second)
    # pointer_3 = None
    # sum_pointer = None
    #
    # while pointer_1 is not None and pointer_2 is not None:
    #     sum = pointer_1.data + pointer_2.data + carry
    #     if sum // 10 > 0:
    #         carry = 1
    #         sum = sum % 10
    #     else:
    #         carry = 0
    #
    #     if pointer_3 is None:
    #         pointer_3 = Node(sum)
    #         sum_pointer = pointer_3
    #     else:
    #         new_node = Node(sum)
    #         pointer_3.next = new_node
    #         pointer_3 = new_node
    #     pointer_1 = pointer_1.next
    #     pointer_2 = pointer_2.next
    #
    # while pointer_1 is not None:
    #     sum = pointer_1.data + carry
    #     if sum // 10 > 0:
    #         carry = 1
    #         sum = sum % 10
    #     else:
    #         carry = 0
    #
    #     if pointer_3 is None:
    #         pointer_3 = Node(sum)
    #         sum_pointer = pointer_3
    #     else:
    #         new_node = Node(sum)
    #         pointer_3.next = new_node
    #         pointer_3 = new_node
    #     pointer_1 = pointer_1.next
    #
    # while pointer_2 is not None:
    #     sum = pointer_2.data + carry
    #     if sum // 10 > 0:
    #         carry = 1
    #         sum = sum % 10
    #     else:
    #         carry = 0
    #
    #     if pointer_3 is None:
    #         pointer_3 = Node(sum)
    #         sum_pointer = pointer_3
    #     else:
    #         new_node = Node(sum)
    #         pointer_3.next = new_node
    #         pointer_3 = new_node
    #     pointer_2 = pointer_2.next
    #
    # if carry != 0:
    #     new_node = Node(carry)
    #     pointer_3.next = new_node
    #     pointer_3 = new_node
    #
    # return reverse_ll(sum_pointer)

#{ 
#  Driver Code Start
#  s
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):

        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)

        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)

        res = addLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends