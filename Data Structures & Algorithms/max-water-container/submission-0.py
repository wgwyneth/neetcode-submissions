class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        maxAreaPointer1 = 0
        maxAreaPointer2 = 1

        for i in range(len(heights)):
            for j in range(i, len(heights)):
                newArea = self.calculateArea(i, j, heights)
                if newArea > maxArea:
                    maxArea = newArea
                    maxAreaPointer1 = i
                    maxAreaPointer2 = j
        return maxArea
    def calculateArea(self, low, high, heights):
        return min(heights[low], heights[high]) * (high - low)