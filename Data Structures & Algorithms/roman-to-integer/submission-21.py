class Solution:
    def romanToInt(self, s: str) -> int:
        numeralMap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            }
        
        integer = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and numeralMap[s[i]] < numeralMap[s[i+1]]:
                integer -= numeralMap[s[i]]
            else:
                integer += numeralMap[s[i]]
        return integer
