class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        unmatched = 0
        for bracket in s:
            if self.isOpenning(bracket):
                stack.append(bracket)
                unmatched += 1
            else:
                if len(stack) != 0:
                    lastBracket = stack.pop()
                    if not self.isMatching(lastBracket, bracket):
                        return False
                    else:
                        unmatched -= 1
                else:
                    return False
        return unmatched == 0

    def isMatching(self, openBracket: str, closeBracket: str) -> bool:
        if openBracket == '(' and closeBracket == ')':
            return True
        elif openBracket == '{' and closeBracket == '}':
            return True
        elif openBracket == '[' and closeBracket == ']':
            return True
        else:
            return False

    def isOpenning(self, bracket) -> bool:
        return bracket in ['(', "{", "["]