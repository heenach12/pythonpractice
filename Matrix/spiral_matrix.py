def spiralOrder(matrix):
    result = []
    n = len(matrix)
    m = len(matrix[0])
    dir = 0
    top = 0
    down = n-1
    left = 0
    right = m-1
    i, j = 0, 0
    k, l = 0, 0
    while(top<=down and left <= right):
        if (dir == 0):
            for i in range(left, right+1, 1):
                result.append(matrix[top][i])
            top += 1
        elif (dir == 1):
            for j in range(top, down+1, 1):
                result.append(matrix[j][right])
            right -= 1
        elif (dir == 2):
            for k in range(right, left-1, -1):
                result.append(matrix[down][k])
            down -= 1
        elif (dir == 3):
            for l in range(down, top-1, -1):
                result.append(matrix[l][left])
            left += 1
        dir = (dir+1)%4
    return result


# Driver code
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

for x in spiralOrder(a):
    print(x, end=" ")
print()
# def spiral_matrix(a, n, m):
#     import pdb; pdb.set_trace()
#     l = []
#     for i in range(n):
#         for j in range(m):
#             l.append(a[i][j])
#             if j == m-1:
#                 while(i<n-1):
#                     l.append(a[i+1][j])
#                     i += 1
#             if i == n-1:
#                 while(j>0):
#                     l.append(a[i][j-1])
#                     j -= 1
#         i = i-1
#         j = 0
#
#     print("l is", l)
#     return l
#
# t = int(input())
# for i in range(t):
#     n = int(input())
#     m = int(input())
#     a = []
#     for i in range(n):
#         l = []
#         for j in range(m):
#             l.append(int(input()))
#         a.append(l)
#
# f = spiral_matrix(a, n, m)
# print("f is ", f)