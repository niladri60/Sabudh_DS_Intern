def unique_word_generator(word_list):
    # Generator function to yield unique words from a list of strings.
    seen = set()
    for word in word_list:
        if word.lower() not in seen:
            seen.add(word.lower())
            yield word

# Test the generator function
test_list = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print("Unique words in the list:")
for word in unique_word_generator(test_list):
    print(word)
