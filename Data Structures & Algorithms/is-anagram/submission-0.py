class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicS = {}
        dicT = {}
        for i in range(len(s)):
            dicS[s[i]] = dicS.get(s[i], 0) + 1
            dicT[t[i]] = dicT.get(t[i], 0) + 1
        
        if len(dicS.keys()) != len(dicT.keys()):
            return False

        for char in dicS.keys():
            sCharNum = dicS.get(char, 0)
            tCharNum = dicT.get(char, 0)
            if sCharNum != tCharNum: 
                return False
        return True
            