# https://leetcode.com/problems/valid-parentheses/

class Solution:
    PARENTHESES = {
        ")" : "(",
        "}" : "{",
        "]" : "[",
    }

    def isValid(self, s: str) -> bool:
        parentheses = []
        open_parentheses = self.PARENTHESES.values()
        for ch in s:
            if ch in open_parentheses:
                parentheses.append(ch)
            else:
                if not parentheses:
                    return False
                last_open = parentheses[-1]
                if self.PARENTHESES[ch] == last_open:
                    parentheses.pop()
                else:
                    return False
        return not parentheses

assert Solution().isValid("()") == True
assert Solution().isValid("()[]{}") == True
assert Solution().isValid("(]") == False
assert Solution().isValid("]") == False
assert Solution().isValid("(])") == False
assert Solution().isValid("[") == False
