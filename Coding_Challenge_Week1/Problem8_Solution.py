def find_median(num1, num2, num3):
  numbers = [num1, num2, num3]
  numbers.sort()
  return numbers[1]

num1 = 15
num2 = 26
num3 = 29
print("Input first number: ",num1)
print("Input second number: ",num2)
print("Input third number: ",num3)
print("Output: ",find_median(num1, num2, num3))

num1 = 10
num2 = 20
num3 = 5
print("Input first number: ",num1)
print("Input second number: ",num2)
print("Input third number: ",num3)
print("Output: ",find_median(num1, num2, num3))

# Output for the above code.

# Input first number:  15
# Input second number:  26
# Input third number:  29 
# Output:  26
# Input first number:  10 
# Input second number:  20
# Input third number:  5  
# Output:  10