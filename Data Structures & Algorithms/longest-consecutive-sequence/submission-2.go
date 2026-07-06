import (
	"cmp"
	"slices"
)
func longestConsecutive(nums []int) int {
	if len(nums) <= 0 {
		return 0
	}
	slices.SortFunc(nums, func(a int, b int) int { return cmp.Compare(a, b)})
	longest := 0
	curr_slice := 0
	prev := -100000
	for _, num := range nums {
		if prev + 1 == num {
			curr_slice += 1 
			longest = max(longest, curr_slice)
			prev = num
		}  else if prev == num{
			prev = num
		}else {
			curr_slice = 0
			prev = num
		}
	}

	return longest + 1
}
