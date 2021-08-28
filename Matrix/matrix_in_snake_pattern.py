def snake_pattern(a):
    n = len(a)
    l = []
    for i in range(n):
        if i%2 == 0:
            for j in range(n):
                l.append(a[i][j])
        else:
            for j in range(n-1, -1, -1):
                l.append(a[i][j])
    return l

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

f = snake_pattern(a)
print("f is", f)
# print_matrix(f, n, n)