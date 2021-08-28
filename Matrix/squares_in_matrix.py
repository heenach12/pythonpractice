class Square_matrix():
    def squaresinmatrix(self, m, n):
        # import pdb; pdb.set_trace()
        list
        max_size = min(m, n)
        min_n = 2
        res = 0
        prod = m*n
        res += prod
        while (min_n < max_size):
            prod = prod//min_n
            res += prod
            # prod =
            min_n += 1

        return res


t = int(input())
for i in range(t):
    m, n = list(map(int, input().strip().split()))
    ob = Square_matrix()
    print(ob.squaresinmatrix(m, n))