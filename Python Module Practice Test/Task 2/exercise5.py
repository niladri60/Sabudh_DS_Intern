def sublist_generator(input_list, n):
    # Generator function to yield all sublists of length n from a list.
    for i in range(len(input_list) - n + 1):
        yield input_list[i:i + n]

# Test the generator function
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Sublists of length 3:")
for sublist in sublist_generator(test_list, 3):
    print(sublist)
