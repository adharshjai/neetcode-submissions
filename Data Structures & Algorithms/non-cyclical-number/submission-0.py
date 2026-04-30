class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        n = str(n)
        while n!="1":
            if n in visited:
                return False
            visited.add(n)
            total = 0
            for c in n:
                total += int(c) **2
            n = str(total)
        return True
            