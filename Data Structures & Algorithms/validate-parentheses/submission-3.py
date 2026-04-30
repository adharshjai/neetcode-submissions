class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchMap = {
            ")":"(", 
            "}":"{", 
            "]":"["
            }

        for char in s:
            if stack and stack[-1] == matchMap.get(char, None):
                stack.pop()
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False


        #stack = [ "[ , (" ] 