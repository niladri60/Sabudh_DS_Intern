def count_vowels_and_consonants(word):
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    
    for char in word.lower():
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
    
    return vowel_count, consonant_count

word = "pythonlobby"
vowels, consonants = count_vowels_and_consonants(word)
print(f"Input: {word}")
print(f"Vowel: {vowels}")
print(f"Consonants: {consonants}")


word = "sabudhfoundation"
vowels, consonants = count_vowels_and_consonants(word)
print(f"\nInput: {word}")
print(f"Vowel: {vowels}")
print(f"Consonants: {consonants}")

# Output of the above code is

# Input: pythonlobby
# Vowel: 2     
# Consonants: 9

# Input: sabudhfoundation
# Vowel: 7
# Consonants: 9