class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        word1 = s
        word2 = t

        if sorted(word1) == sorted(word2):
            return True
        else:
            return False
