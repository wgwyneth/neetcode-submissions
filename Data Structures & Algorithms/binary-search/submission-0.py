class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchHelper(0, len(nums) -1, nums, target)

    def searchHelper(self, low: int, high: int, nums: List[nums], target: int) -> int:
        if high >= low:
            midpoint = low + (high - low) // 2

            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                return self.searchHelper(low, midpoint -1, nums, target)
            else:
                return self.searchHelper(midpoint + 1, high, nums, target)
        return -1