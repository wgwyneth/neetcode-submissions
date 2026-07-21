class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPositions = []
        carStack = []
        for i in range(len(position)):
            sortedPositions.append((position[i], speed[i]))

        sortedPositions.sort(key=lambda touple: touple[0], reverse=True)
       
        for i in range(len(sortedPositions)):
            p = sortedPositions[i][0]
            s = sortedPositions[i][1]
            carStack.append((target - p) / s)
            if len(carStack) >= 2 and carStack[-1] <= carStack[-2]:
                carStack.pop()

        return len(carStack)


        
            