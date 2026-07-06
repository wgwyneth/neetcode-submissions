func productExceptSelf(nums []int) []int {
	prefix := make([]int, len(nums))
	suffix := make([]int, len(nums))

	returns := make([]int, len(nums))

	for i := range nums {
		if i == 0 {
			prefix[i] = 1
		} else {
			prefix[i] = nums[i - 1] * prefix[i - 1]
		}
	}

	for i := len(nums) - 1; i >= 0; i-- {
		if i == len(nums) - 1{
			suffix[i] = 1
		} else {
			suffix[i] = nums[i + 1] * suffix[i + 1]
		}
	} 

	for i := range prefix {
		returns[i] = prefix[i] * suffix[i]
	}

	return returns
}
