class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arrS, arrT = {}, {}

        #add the count of each character to a hashmap and then return arrS == arrT

        for char in s:
            arrS[char] = arrS.get(char, 0) + 1
        
        for char in t:
            arrT[char] = arrT.get(char, 0) + 1
        
        return arrS == arrT