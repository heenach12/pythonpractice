def winner_election(a, n):
    h_map = {}
    for i in a:
        if i not in a:
            h_map[i] = 1
        else:
            h_map[i] += 1

    f = max(list(h_map.values())
    h = []
    for k, v in h_map.items():
        if
    v == f:
    h.append(k)

    for i in range(n):
        pass

    j = h.sort(key=len)
    i = [j, f]
    print("i is", i)
    return i


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    r = winner_election(a, n)
    print("res", r[0], r[1])