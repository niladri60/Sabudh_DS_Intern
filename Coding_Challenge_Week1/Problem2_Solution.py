def remove_duplicates(input_string):
    seen = set()
    result = []
    
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

# Test cases
test_cases = [
    "abaabbbacd",
    "ddeefggh"
]

for test in test_cases:
    output = remove_duplicates(test)
    print(f"Input: {test}")
    print(f"Output: {output}")


# Output of the above code.

# Input: abaabbbacd
# Output: abcd
# Input: ddeefggh
# Output: defgh