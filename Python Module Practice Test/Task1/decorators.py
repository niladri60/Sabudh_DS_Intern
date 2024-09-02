import time
from functools import wraps

# Define the uppercase_decorator
def uppercase_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result
    return wrapper

# Define the say_hello function
def say_hello(name):
    return f"Hello, {name}!"

# Apply the uppercase_decorator to the say_hello function
greet = uppercase_decorator(say_hello)

# Test the greet function
print(greet("Niladri"))  # Output should be in uppercase: "HELLO, ALICE!"

# Define the timing_decorator
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to run.")
        return result
    return wrapper

# Apply the timing_decorator to the greet function
timed_greet = timing_decorator(greet)

# Test the timed_greet function
print(timed_greet("Nandy"))  # Output should show the time taken and the greeting in uppercase

# Define the logging_decorator
def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called with arguments {args}, {kwargs} and returned {result}")
        return result
    return wrapper

# Define the Math class with add and subtract methods
class Math:

    @staticmethod
    @logging_decorator  # Apply the decorator here
    def add(a, b):
        return a + b

    @staticmethod
    @logging_decorator  # Apply the decorator here
    def subtract(a, b):
        return a - b

# Test the Math class methods
math_instance = Math()
print(math_instance.add(5, 3))        # Output should log the call and return 8
print(math_instance.subtract(10, 4))  # Output should log the call and return 6
