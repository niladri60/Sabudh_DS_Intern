def single_number(nums):
    # Step 1: XOR all the numbers
    xor_result = 0
    for num in nums:
        xor_result ^= num
    
    # Step 2: Find the rightmost set bit in xor_result
    diff_bit = xor_result & -xor_result  # This isolates the rightmost set bit
    
    # Step 3: Divide the numbers into two groups and XOR the numbers in each group
    num1, num2 = 0, 0
    for num in nums:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num
    
    return [num1, num2]

# Test case 1
nums1 = [1, 2, 1, 3, 2, 5]
print(f"Input: {nums1}, Output: {single_number(nums1)}")  # Output: [3, 5]

# Test case 2
nums2 = [-1, 0]
print(f"Input: {nums2}, Output: {single_number(nums2)}")  # Output: [-1, 0]

# Test case 3
nums3 = [0, 1]
print(f"Input: {nums3}, Output: {single_number(nums3)}")  # Output: [1, 0]

# Output
# Input: [1, 2, 1, 3, 2, 5], Output: [3, 5]
# Input: [-1, 0], Output: [-1, 0]
# Input: [0, 1], Output: [1, 0]