func twoSum(nums []int, target int) []int {
    hashy := make(map[int]int)
    returns := []int{}
    for i, num := range nums {
        otherIndex, ok := hashy[target - num]
        if ok {
            return append(returns, otherIndex, i)
        } else {
            hashy[num] = i
        }
    } 

    return returns
}
