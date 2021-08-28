"""Find next smaller element to the right, same approach as next_greater element"""
def next_smaller_element(arr, n):
    rb = [0] * n
    st = []
    st.append(arr[n-1])
    rb[len(arr) - 1] = len(arr)

    for i in range(n-2, -1, -1):
        while(len(st) > 0 and arr[i] < st[-1]):
            st.pop()

        if len(st) == 0:
            rb[i] = n
        else:
            rb[i] = st[-1]

        st.append(arr[i])
    print("rb is", rb)
    return rb

arr = [6, 2, 5, 4, 5, 1, 6]
n = 7

print(next_smaller_element(arr, n))
