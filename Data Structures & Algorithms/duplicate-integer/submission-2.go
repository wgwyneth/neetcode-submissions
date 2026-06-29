
func hasDuplicate(nums []int) bool {
    
    m := make(map[int]int)

    for _, element := range nums {
        _, ok := m[element]
        if ok {
            fmt.Printf("Found duplicate element: %v", element)
            return true
        } else {
            m[element] = 1
        }
    }

    return false
}
