class CheckPermutation:
    def solution1(self, a: string, b: string) -> bool:
        wordA = {}
        wordB = {}

        for charA in a:
            wordA[charA] = wordA.get(charA, 0) + 1

        for charB in b:
            wordB[charB] = wordB.get(charB, 0) + 1

        if len(wordA.keys()) != len(wordB.keys()):
            return False
        
        for charA in wordA.keys():
            if wordA[charA] != wordB.get(charA, 0):
                return False

        for charB in wordB.keys():
            if wordB[charB] != wordA.get(charB, 0):
                return False

        return True

    def printProblem(self, inputA: string, inputB: string) -> None:
        print("String A:", inputA, "String B:", inputB, "Results:", str(self.solution1(inputA, inputB)))

if __name__ == '__main__':
    problemSolver = CheckPermutation()
    problemSolver.printProblem("abcd", "dcba")
    problemSolver.printProblem("Duck", "Goose")
    problemSolver.printProblem("tacocat", "tacocat")
    
            
