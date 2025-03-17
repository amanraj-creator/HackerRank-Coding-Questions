'''
Problem Statement:
Implement a function that takes a string consisting of words separated by single spaces and returns a string containing 
all those words but in the reverse order. Additionally, all cases of letters in the original string should be 
swapped — lowercase letters become uppercase, and uppercase letters become lowercase.

Example:
sentence = "rUns dOg"
Output:
"DoG RuNS"

'''

def reverse_and_swap(sentence):
    return ' '.join(sentence.swapcase().split()[::-1])  # Corrected to return a string

# Example usage
sentence = "aWESOME is cODING"
result = reverse_and_swap(sentence)
print(result)  # Output: "CoDING IS Awesome"
