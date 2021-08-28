def histogram_area(arr):
    n = len(arr)
    rb = [0] * n

    lb = [0] * n

    st_r = []
    st_r.append(n-1)
    rb[n-1] = n

    for i in range(n-2, -1, -1):
        while (len(st_r) > 0 and arr[i] < arr[st_r[-1]]):
            st_r.pop()

        if len(st_r) == 0:
            rb[i] = n
        else:
            rb[i] = st_r[-1]

        st_r.append(i)

    stl = []
    stl.append(0)
    lb[0] = -1

    for j in range(1, n):
        while ( len(stl) > 0 and arr[j] < arr[stl[-1]]):
            stl.pop()

        if len(stl) == 0:
            lb[j] = -1
        else:
            lb[j] = stl[-1]

        stl.append(j)

    maxarea = 0

    for i in range(n):
        width = rb[i] - lb[i] - 1
        area = arr[i] * width
        if area > maxarea:
            maxarea = area

    return maxarea

arr = [6, 2, 5, 4, 5, 1, 6]
print(histogram_area(arr))