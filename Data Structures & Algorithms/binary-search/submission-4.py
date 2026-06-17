class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftBar = 0
        rightBar = len(nums) - 1
        while leftBar <= rightBar:
            midBar = leftBar + ((rightBar - leftBar) // 2)
            
            if nums[midBar] > target:
                rightBar = midBar - 1
            elif nums[midBar] < target:
                leftBar = midBar + 1 
            else:
                return midBar
        return -1 #the dreaded no bar