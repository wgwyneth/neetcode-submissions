class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        frequencyKeys = list(frequency.keys())
        frequencyKeys.sort(key=lambda x:frequency[x], reverse=True)

        return frequencyKeys[:k]
            