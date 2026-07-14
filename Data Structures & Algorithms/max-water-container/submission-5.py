class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        left = 0 
        right = len(heights) - 1

        while left <= right:
            currArea = self.findArea(left, right, heights)

            if currArea > maxArea:
                maxArea = currArea

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1
        
        return maxArea
        


    def findArea(self, left: int, right: int, heights: List[int]) -> int:
        height = min(heights[left], heights[right])
        length = right - left
        return height * length