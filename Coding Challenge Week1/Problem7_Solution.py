def print_odd_index_elements(my_list):

    for i in range(1, len(my_list), 2):
        print(my_list[i], end=" ")
    print()

# Test cases
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Input: ", list1)
print("Output: ", end="")
print_odd_index_elements(list1)

print("\n")

list2 = [23, 46, 69, 92, 115]
print("Input: ", list2)
print("Output: ", end="")
print_odd_index_elements(list2)


# Output for the above code.
# Input:  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Output: 20 40 60 80 100 


# Input:  [23, 46, 69, 92, 115]       
# Output: 46 92 