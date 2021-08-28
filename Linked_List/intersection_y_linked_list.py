"""def getCount(head):
    temp = head
    c = 0
    while(temp):
        c += 1
        temp = temp.next

    return c

def intersetPoint(head1,head2):
    c1 = getCount(head1)
    c2 = getCount(head2)

    h1 = head1
    h2 = head2
    d = abs(c1-c2)

    if c1 > c2:
        for i in range(d):
            h1 = h1.next
    else:
        for i in range(d):
            h2 = h2.next

    while(h1 != h2):
        h1 = h1.next
        h2 = h2.next

    return h1.data
"""

def getCount(head):
    temp = head
    c = 0
    while (temp):
        c += 1
        temp = temp.next

    return c


def intersetPoint(head1, head2):
    c1 = getCount(head1)
    c2 = getCount(head2)

    h1 = head1
    h2 = head2
    d = abs(c1 - c2)

    if c1 > c2:
        for i in range(d):
            h1 = h1.next
    else:
        for i in range(d):
            h2 = h2.next

    while (h1 != h2):
        h1 = h1.next
        h2 = h2.next

    return h1.data
