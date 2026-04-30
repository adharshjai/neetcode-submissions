class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        strs, strt = {}, {}

        for i in range(len(s)):
            strs[s[i]] = 1 + strs.get(s[i], 0)
            strt[t[i]] = 1 + strt.get(t[i], 0)
        
        return strs == strt