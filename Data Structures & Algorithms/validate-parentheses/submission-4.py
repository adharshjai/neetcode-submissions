class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchMap = {
            ")":"(", 
            "}":"{", 
            "]":"["
            }

        for char in s:
            if char in "])}" and stack and stack[-1] == matchMap[char]:
                stack.pop()
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False


        #stack = [ "[ , (" ] 