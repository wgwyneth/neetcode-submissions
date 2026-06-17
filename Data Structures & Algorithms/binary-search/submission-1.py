class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchHelper(0, len(nums) - 1, nums, target)
    
    def searchHelper(self, left: int, right: int, nums: list[int], target: int) -> int:
        midpoint = left + (right - left) // 2
        if right >= left:
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target: 
                return self.searchHelper(left, midpoint - 1, nums, target)
            else:
                return self.searchHelper(midpoint + 1, right, nums, target)
        return -1