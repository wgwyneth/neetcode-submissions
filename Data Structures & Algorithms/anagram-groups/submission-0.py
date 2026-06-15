class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charPositionMap = {}
        chars = "abcdefghijklmnopqrstuvwxyz"
        for i in range(26):
            charPositionMap[chars[i]] = i

        anagramToString = {}
        for stry in strs:
            frequencyArr = [0] * 26
            for letter in stry:
              frequencyArr[charPositionMap[letter]] += 1
            listToAppend = anagramToString.get(tuple(frequencyArr), [])
            if listToAppend == None:
                listToAppend = [stry]
            else:
                listToAppend.append(stry)
            anagramToString[tuple(frequencyArr)] = listToAppend
    
        returns = [] 
        for anagramKey in anagramToString.keys():
            returns.append(anagramToString[anagramKey])
        return returns
        