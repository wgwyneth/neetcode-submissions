class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = set()
        for num in nums:
            newSet.add(num)
        return len(newSet) != len(nums)
        