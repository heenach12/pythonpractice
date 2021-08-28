class CountZero():
    def count_zeros(self, arr, n):
        res = 0

        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0:
                    res+=1
        return res


t = int(input())
for i in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    mat = [[0 for x in range(n)] for y in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            mat[i][j] = arr[k]
            k+=1
    ob = CountZero()
    print(ob.count_zeros(mat, n))