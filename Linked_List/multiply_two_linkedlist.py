def multiply_ll(first, second):
    n1 = 0
    n2 = 0
    MOD = 10**9+7

    while (first or second):
        if (first):
            n1 = ((n1*10)+first.data)%MOD
            first = first.next
        if (second):
            n2 = (n2 * 10 + second.data) % MOD
            second = second.next

    g = ((n1 % MOD) * (n2 % MOD)) % MOD
    return g
