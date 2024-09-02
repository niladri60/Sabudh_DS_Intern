def word_generator(input_string):
    """Generator function to yield words from a string."""
    words = input_string.split()
    for word in words:
        yield word

# Test the generator function
test_string = "The quick brown fox jumps over the lazy dog."
print("Words in the string:")
for word in word_generator(test_string):
    print(word)
