def remove_duplicates(s: str) -> str:
    stack = []
    
    # Iterate through the string
    for char in s:
        if stack and stack[-1] == char:
            # Remove the top of the stack if it's a duplicate
            stack.pop()
        else:
            # Add the character to the stack
            stack.append(char)
    
    # Join the characters in the stack to form the final string
    return ''.join(stack)

# Test case 1
s1 = "abbaca"
print(f'Input: "{s1}", Output: "{remove_duplicates(s1)}"')  # Output: "ca"

# Test case 2
s2 = "azxxzy"
print(f'Input: "{s2}", Output: "{remove_duplicates(s2)}"')  # Output: "ay"


# Output
# Input: "abbaca", Output: "ca"
# Input: "azxxzy", Output: "ay"