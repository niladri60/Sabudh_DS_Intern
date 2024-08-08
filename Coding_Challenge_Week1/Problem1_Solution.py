def print_squares(n):

  if n <= 0:
    print("Error: Input must be a positive integer.")
    return

  squares = [i**2 for i in range(n)]
  print(squares)

# Test cases
n1 = 5
print("Input: ", n1)
print_squares(n1)  # Output: [0, 1, 4, 9, 16]

n2 = 4
print("Input: ", n2)
print_squares(n2)  # Output: [0, 1, 4, 9]
