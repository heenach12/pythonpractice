"""A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.


Example 1:

Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0},
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity."""
class Solution:
    def celebrity(self, arr, n):
        # ans = -1
        #
        # for i in range(n):
        #     c = 0
        #     for j in arr[i]:
        #         if j == 0:
        #             c += 1
        #         else:
        #             break
        #
        #     if c == n and ans == -1:
        #         ans = i
        #     elif c == n:
        #         return -1
        #
        # return ans

        # import pdb; pdb.set_trace()
        s = []
        for i in range(n):
            s.append(i)
        # print("s is", s)
        while(len(s) >= 2):
            i = s.pop()

            j = s.pop()
            # print("i, j", i, j)
            if arr[i][j] == 1:
                s.append(j)
            else:
                s.append(i)
            # print("now s is", s)
        # if len(s) >= 1:

        pot = s.pop()
        # print("potential is", pot)
        for i in range(n):
            if (i !=  pot):
                if (arr[i][pot] == 0 or arr[pot][i] == 1):
                    return -1

        return pot


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = 0
    m = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(arr[k])
            k += 1
        m.append(r)
    ob = Solution()
    print(ob.celebrity(m, n))