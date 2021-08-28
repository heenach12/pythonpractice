def reverse_ll(head):
    if head is None:
        return None

    if head.next is None:
        return  head

    prev= None
    curr = head
    next = None

    while(curr is not None):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

def add_number(head):
    f = reverse_ll(head)
    carry = 0
    head.data += 1
    prev = None

    while(head != None) and (head.data > 9 or carry > 0):
        prev = head
        head.data += carry
        carry = head.data // 10
        head.data = head.data % 10
        head = head.next

    if carry > 0:
        prev.next = Noed(carry)
    return reverse_ll(k)
