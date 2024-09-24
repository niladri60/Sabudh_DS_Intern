def trap(height):
    if not height:
        return 0

    n = len(height)
    
    # Step 1: Create left max and right max arrays
    left_max = [0] * n
    right_max = [0] * n
    
    # Step 2: Fill the left max array
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
    
    # Step 3: Fill the right max array
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    
    # Step 4: Calculate the trapped water
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]
    
    return trapped_water

# Test case 1
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"Input: {height1}, Output: {trap(height1)}")  # Output: 6

# Test case 2
height2 = [4, 2, 0, 3, 2, 5]
print(f"Input: {height2}, Output: {trap(height2)}")  # Output: 9
