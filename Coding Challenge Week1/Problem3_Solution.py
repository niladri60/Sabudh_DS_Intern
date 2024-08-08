def filter_numbers(numbers):
    result = []
    for number in numbers:
        if number > 500:
            break
        if number > 150:
            continue
        if number % 5 == 0:
            result.append(number)
    return result

# Test cases
test_cases = [
    [12, 75, 150, 180, 145, 525, 50],
    [14, 85, 625, 75]
]

for test in test_cases:
    output = filter_numbers(test)
    print(f"Input : {test}")
    print(f"Output : {output}")


# Output of the above code.

# Input : [12, 75, 150, 180, 145, 525, 50]
# Output : [75, 150, 145]
# Input : [14, 85, 625, 75]
# Output : [85]