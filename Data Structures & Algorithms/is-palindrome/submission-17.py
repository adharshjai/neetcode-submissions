class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        sList = []

        for char in lower:
            if char.isalnum():
                sList.append(char)
        
        l, r = 0, len(sList)-1
            
        for i in range(len(sList)):
            if sList[l] != sList[r]:
                return False
            l += 1
            r -= 1
        
        return True





        
                