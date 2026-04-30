class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        word1 = Counter(s)
        word2 = Counter(t)

        if word1 == word2:
            return True
        else:
            return False
