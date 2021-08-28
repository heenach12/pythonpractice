def transpose_matrix(a, n, m):
    for i in range(n):
        for j in range(i, m):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a
    # B = [[0 for x in range(n)] for y in range(m)]
    # for i in range(n):
    #     for j in range(m):
    #         B[i][j] = a[j][i]
    # return B

t = int(input())
for i in range(t):
    n = int(input())
    m = int(input())
    a = []
    for i in range(n):
        l = []
        for j in range(m):
            l.append(int(input()))
        a.append(l)



print("Now printing the matrix")
def print_matrix(a, n, m):
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=" ")
        print(" ")

f = transpose_matrix(a, n, m)
print("f is", f)
g = print_matrix(f, n, m)
