"""Given two linked lists, your task is to complete the function makeUnion(), that returns the union of two linked lists. This union should include all the distinct elements only.

Example 1:

Input:
L1 = 9->6->4->2->3->8
L2 = 1->2->8->6->2
Output: 1 2 3 4 6 8 9
Your Task:
The task is to complete the function makeUnion() which makes the union of the given two lists and returns the head of the new list.

Note: The new list formed should be in non-decreasing order."""
def unionLinkedlist(head1, head2):
    if head1 is None or head2 is None:
        return

    f1 = head1
    f2 = head2

    s = set()
    while(f1):
        s.add(f1.data)
        f1 = f1.next

    while(f2):
        s.add(f2.data)
        f2 = f2.next

    s = sorted(s)
    ll = Linked_List()
    ll.head = s[0]
    a = ll.head

    for i in range(1, len(s)):
        new_node = Node(s[i])
        new_node.next = ll.head.next
        ll.head.next = new_node
        ll.head = ll.head.next

    ll.head = a
    return ll.head
