# Generators in Python Assignment

## Description

This assignment explores the concept of generators in Python, a powerful feature that allows for efficient iteration over sequences without loading the entire sequence into memory.

## Approach and Challenges

### 1. Fibonacci Sequence Generator (`exercise1.py`)

- **Approach:** We used two variables `a` and `b` to hold the current and next Fibonacci numbers and iterated `n` times to yield each number.
- **Challenges:** Managing the state of two variables in a generator function was straightforward; however, the challenge was ensuring that the generator stopped after yielding `n` numbers.

### 2. Prime Numbers Generator (`exercise2.py`)

- **Approach:** A helper function `is_prime` was used to check primality, and the main generator function iterated through numbers up to `n` and yielded primes.
- **Challenges:** Optimizing the prime-checking function was necessary to handle larger numbers efficiently.

### 3. Word Generator from String (`exercise3.py`)

- **Approach:** The input string was split into words, and each word was yielded in sequence.
- **Challenges:** Handling punctuation and different types of whitespace was considered but kept simple for this assignment.

### 4. Unique Words Generator from List (`exercise4.py`)

- **Approach:** Used a set to track seen words and yielded words that had not been seen before.
- **Challenges:** Dealing with case sensitivity was important, so all words were converted to lowercase before checking.

### 5. Sublists Generator from List (`exercise5.py`)

- **Approach:** Iterated over the input list using a sliding window to yield sublists of length `n`.
- **Challenges:** Ensuring correct index handling to avoid `IndexError` when reaching the end of the list.

## How to Run

To run each exercise, simply execute the corresponding Python file in your terminal:

```bash
python exercise1.py
python exercise2.py
python exercise3.py
python exercise4.py
python exercise5.py
```

With these Python files and the `README.md` file, you should be able to understand and execute each generator function as required by the assignment.
