class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -1
        maxLeftPointer = 0
        maxRigthPointer = 0
        leftPointer = 0
        rightPointer = len(heights) - 1

        while(leftPointer != rightPointer):
            currArea = self.area(leftPointer, rightPointer, heights)
            if currArea > maxArea:
                maxArea = currArea
                maxLeftPointer = leftPointer
                maxRightPointer = rightPointer

            if heights[leftPointer] > heights[rightPointer]:
                rightPointer -= 1
            else:
                leftPointer += 1
            
        return maxArea
    def area(self, left: int, right: int, heights: list[int]) -> int:
        return min(heights[left], heights[right]) * (right - left)
        