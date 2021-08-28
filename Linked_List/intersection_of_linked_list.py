def findIntersection(head1, head2):
    if head1 is None or head2 is None:
        return

    s1 = set()
    s2 = set()

    f1 = head1
    f2 = head2

    while(f2):
        s2.add(f2.data)
        f2 = f2.next

    ll = Linked_List()
    while(f1 is not None):
        if f1.data not in s1:
            if f1.data in s2:
                if ll.head is None:
                    ll.head = Node(f1.data)
                    a = ll.head
                else:
                    new_node = Node(f1.data)
                    new_node.next = ll.head.next
                    ll.head.next = new_node
                    ll.head = ll.head.next
        else:
            s1.add(f1.data)
        f1 = f1.next
        ll.head = a
        return ll.head