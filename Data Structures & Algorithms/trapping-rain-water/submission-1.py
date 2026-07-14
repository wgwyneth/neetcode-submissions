class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                leftMax[0] = height[0]
            else:
                leftMax[i] = max(leftMax[i - 1], height[i])
            
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                rightMax[i] = height[i]
            else:
                rightMax[i] = max(rightMax[i + 1], height[i])

        maxArea = 0
        for i in range(len(height)):
            maxArea += min(leftMax[i], rightMax[i]) - height[i]

        return maxArea
