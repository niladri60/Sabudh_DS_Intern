def reverse_number(num):

  reversed_num = 0
  while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
  return reversed_num

# Test cases
num1 = 745633
print("Input: ", num1)
print("Output: ", reverse_number(num1))

print("\n")

num2 = 65346
print("Input: ", num2)
print("Output: ", reverse_number(num2))

# Output for the above code

# Input:  745633
# Output:  336547


# Input:  65346
# Output:  64356
