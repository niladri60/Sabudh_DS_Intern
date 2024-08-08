def factorial(n):
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")

  elif n == 0 or n == 1:
    return 1
  else:
    result = 1
    for i in range(2, n + 1):
      result *= i
    return result
  
input_number = 4
output = factorial(input_number)
print("Input: ",input_number)
print(f"Factorial of {input_number}: {output}")

input_number = 2
output = factorial(input_number)
print("Input: ",input_number)
print(f"Factorial of {input_number}: {output}")

# Output of the above code
# Input:  4
# Factorial of 4: 24
# Input:  2
# Factorial of 2: 2