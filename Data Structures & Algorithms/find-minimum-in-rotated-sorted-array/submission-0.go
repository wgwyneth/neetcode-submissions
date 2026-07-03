func findMin(nums []int) int {
	left := 0
	right := len(nums) - 1

	for left < right {
		midpoint := left + (right -  left) / 2
		
		midValue := nums[midpoint]
		rightValue := nums[right]

		if midValue < rightValue {
			right = midpoint
		} else {
			left = midpoint + 1
		}
	}

	return nums[left]
}
