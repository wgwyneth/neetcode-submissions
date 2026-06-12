class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                stackT, stackInd = stack.pop()
                results[stackInd] = i - stackInd
            stack.append((temperatures[i], i))
        return results

