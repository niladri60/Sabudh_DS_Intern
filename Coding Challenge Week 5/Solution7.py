def maxSubArray(nums):
    # Initialize the variables
    current_sum = max_sum = nums[0]
    
    # Start from the second element since we initialized the first one
    for num in nums[1:]:
        # Either extend the current subarray or start a new subarray with the current element
        current_sum = max(num, current_sum + num)
        
        # Update the global maximum if needed
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example 1
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Input: {nums1}, Output: {maxSubArray(nums1)}")  # Output: 6

# Example 2
nums2 = [1]
print(f"Input: {nums2}, Output: {maxSubArray(nums2)}")  # Output: 1

# Example 3
nums3 = [5, 4, -1, 7, 8]
print(f"Input: {nums3}, Output: {maxSubArray(nums3)}")  # Output: 23
