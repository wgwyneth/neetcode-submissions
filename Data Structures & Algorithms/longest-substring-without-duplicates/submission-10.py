class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        left = 0
        returns = 0

        for right in range(len(s)):
            if s[right] in substring:
                left = max(substring[s[right]] + 1, left)
            substring[s[right]] = right
            returns = max(returns, right - left + 1)
        return returns