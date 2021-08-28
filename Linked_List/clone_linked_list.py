def clone_linked(head):
    curr = head
    while(curr is not None):
        new = Node(curr.data)
        new.next = curr.next
        curr.next = new
        curr = curr.next.next

    curr = head
    while(curr is not None):
        curr.next.arb = curr.arb.next
        curr = curr.next.next

    curr = head
    dup = head.next

    while (curr.next != None):
        tmp = curr.next
        curr.next = curr.next.next
        curr = tmp

    return dup

