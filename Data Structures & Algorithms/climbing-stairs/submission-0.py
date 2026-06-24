class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * n

        for i in range(n):
            if i == 0:
                memo[i] = 1
            elif i == 1:
                memo[i] = 2
            else:
                memo[i] = memo[i - 2] + memo[i - 1]

        return memo[-1]
