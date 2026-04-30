class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchMap = {")":"(", "}":"{" , "]":"["}

        for c in s:
            if c in matchMap:
                if stack and stack[-1] == matchMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
