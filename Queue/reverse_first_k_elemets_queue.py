"""Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

enqueue(x) : Add an item x to rear of queue
dequeue() : Remove an item from front of queue
size() : Returns number of elements in queue.
front() : Finds front item.
Example 1:

Input:
5 3
1 2 3 4 5

Output:
3 2 1 4 5

Explanation:
After reversing the given
input from the 3rd position the resultant
output will be 3 2 1 4 5.
"""

def reverse_k(q, k):
    st = []
    st.remove("a")

    q2 = q[k:]

    for i in range(k):
        f = q.pop(0)
        st.append(f)

    q = []

    for i in range(k):
        f = st.pop()
        q.append(f)

    q = q + q2

    return q

q = [1,2,3,4,5]
k = 3
print(reverse_k(q, k))