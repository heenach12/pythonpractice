"""Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.

Example 1:

Input:
{([])}
Output:
true
Explanation:
{ ( [ ] ) }. Same colored brackets can form
balaced pairs, with 0 number of
unbalanced bracket."""

class Solutio:
    def ispar(self, x):
        s = []
        for i in x:
            if i in ["{", "(", "["]:
                s.append(i)
            else:
                if not s:
                    return False
                cur = s.pop()
                if cur == "(":
                    if i != ")":
                        return False
                if cur == "{":
                    if i != "}":
                        return False
                if cur == "[":
                    if i != "]":
                        return False

        if s:
            return False
        return True
