class SparseVector:
    def __init__(self, nums):
        # Store non-zero elements in the form of index-value pairs
        self.non_zero_elements = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec):
        result = 0
        # Iterate over the non-zero elements of this vector
        for i, value in self.non_zero_elements.items():
            if i in vec.non_zero_elements:
                result += value * vec.non_zero_elements[i]
        return result

# Example 1
nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(f"Output: {v1.dotProduct(v2)}")  # Output: 8

# Example 2
nums1 = [0, 1, 0, 0, 0]
nums2 = [0, 0, 0, 0, 2]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(f"Output: {v1.dotProduct(v2)}")  # Output: 0

# Example 3
nums1 = [0, 1, 0, 0, 2, 0, 0]
nums2 = [1, 0, 0, 0, 3, 0, 4]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(f"Output: {v1.dotProduct(v2)}")  # Output: 6