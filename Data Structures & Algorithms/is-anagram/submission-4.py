class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        t1 = sorted(t)
        if len(s) != len(t):
            return False

        return s1 == t1
