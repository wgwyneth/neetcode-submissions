import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = "[^a-zA-Z0-9]"
        sReplaced = re.sub(pattern, "", s)
        sRepalced = sReplaced.lower()
        forwardPointer = 0
        backPointer = len(sReplaced) - 1
        while(backPointer != forwardPointer):
            if (backPointer <= -1) or (forwardPointer >= len(sReplaced) - 1):
                break
            if sReplaced[forwardPointer].lower() == sReplaced[backPointer].lower():
                forwardPointer += 1
                backPointer -= 1
                
            else:
                return False
        return True