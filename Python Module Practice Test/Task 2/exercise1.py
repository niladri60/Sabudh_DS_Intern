def fibonacci_generator(n):
    """Generator function to generate the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Test the generator function
print("First 10 Fibonacci numbers:")
for number in fibonacci_generator(10):
    print(number)
