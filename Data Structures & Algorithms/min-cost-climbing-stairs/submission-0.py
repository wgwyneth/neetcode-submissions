class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * len(cost)
        
        for i in range(len(cost)):
            if i == 0 or i == 1:
                memo[i] = cost[i]
            else:
                memo[i] = min(memo[i - 1] + cost[i], memo[i - 2] + cost[i])

            print(memo)

        return min(memo[-1], memo[-2])