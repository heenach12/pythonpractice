"""You are given a string S, the task is to reverse the string using stack.
Example 1:

Input: S="GeeksforGeeks"
Output: skeeGrofskeeG
"""

def reverse(S):
    st = []
    out = ""
    for i in S:
        st.append(i)

        # print("st is", st)
    for i in range(len(st)):
        out += st.pop()

    return out

t = int(input())
for i in range(t):
    s = input()
    print(reverse(s))