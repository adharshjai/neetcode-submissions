class Solution:
    def isPalindrome(self, s: str) -> bool:
        sort =  ""
        
        for c in s:
            if c.isalnum():
                sort += c.lower()

        l, r = 0, (len(sort)-1)

        while l <= r:
            for i in range(len(sort)):
                if sort[l] != sort[r]:
                    return False
                l += 1
                r -= 1
        
        return True