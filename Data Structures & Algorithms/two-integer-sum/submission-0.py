class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for i in range(len(nums)):
            hashy[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashy and hashy[diff] != i:
                return [i, hashy[diff]]
        return []
        