class Solution:
    def isOpen(self, s):
        if s in ['(', '[', '{']:
            return True

    def isMatchedBracket(self, s1, s2):
        if s1 == '(' and s2 == ')':
            return True
        elif s1 == '{' and s2 == '}':
            return True
        elif s1 == '[' and s2 == ']':
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        stack = []
        unmatched = 0
        for bracket in s:
            print(bracket)
            if self.isOpen(bracket):
                stack.append(bracket)
                unmatched += 1
            else:
                if len(stack) == 0:
                    return False

                oldBracket = stack.pop()
                
                if not self.isMatchedBracket(oldBracket, bracket):
                    return False
                unmatched -= 1
        if unmatched == 0:
            return True
        return False