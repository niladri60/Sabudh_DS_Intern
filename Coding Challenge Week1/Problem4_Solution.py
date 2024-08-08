def count_digits(number):
    count = 0
    while number != 0:
        number //= 10  # Floor division to remove the last digit
        count += 1
    return count

# Test cases
test_cases = [
    75869,
    654
]

for test in test_cases:
    output = count_digits(test)
    print(f"Input: {test}")
    print(f"Output: {output}")


# Output of the above code.

# Input: 75869
# Output: 5
# Input: 654
# Output: 3