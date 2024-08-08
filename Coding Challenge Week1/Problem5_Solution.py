def sum_of_series(n):
    total = 0
    number = 0

    for i in range(n):
        number = number * 10 + 2
        total += number

    return total

n = 5
print("Input ",n)
print(f"Output : {sum_of_series(n)}")

n=6
print("Input ",n)
print(f"Output : {sum_of_series(n)}")

# Output for the above code

# Input  5
# Output : 24690
# Input  6
# Output : 246912