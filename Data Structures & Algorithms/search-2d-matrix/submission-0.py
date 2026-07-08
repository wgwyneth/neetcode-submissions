class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = []
        for row in matrix: 
            flattened += row

        left = 0
        right = len(flattened) - 1
        while left <= right:
            center = left + (right - left) // 2
            midpoint = flattened[center]
            if midpoint < target: 
                left = center + 1
            elif midpoint > target: 
                right = center - 1
            else:
                return True
        
        return False
