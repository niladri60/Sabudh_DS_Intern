def prime_generator(n):
    """Generator function to generate all prime numbers up to n."""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in range(2, n + 1):
        if is_prime(num):
            yield num

# Test the generator function
print("Prime numbers up to 100:")
for prime in prime_generator(100):
    print(prime)
