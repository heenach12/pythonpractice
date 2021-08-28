def longest_valid_paranthesis(stri):
    # st = []
    # st.append(-1)
    #
    # max_num = 0
    # for i in range(len(stri)):
    #     c = stri[i]
    #     if c == "(":
    #         st.append(i)
    #     else:
    #         st.pop()
    #         if len(st) == 0:
    #             st.append(i)
    #         else:
    #             long_v = i - st[-1]
    #             max_num = max(max_num, long_v)
    #
    # return max_num


    """Below approach is also working"""

    # import pdb; pdb.set_trace()
    open_p = 0
    close = 0
    maxn = 0
    for i in range(len(stri)):
        ct = stri[i]
        if ct == "(":
            open_p += 1
        else:
            close += 1

        if open_p == close:
            l = open_p + close
            maxn = max(maxn, l)
        elif (close > open_p):
            open_p = 0
            close = 0

    open_p = 0
    close = 0

    for j in range(len(stri) - 1, -1, -1):
        ct = stri[j]
        if ct == "(":
            open_p += 1
        else:
            close += 1

        if open_p == close:
            l = open_p + close
            maxn = max(maxn, l)
        elif (open_p > close):
            open_p = 0
            close = 0

    return maxn


s = input()
print(longest_valid_paranthesis(s))