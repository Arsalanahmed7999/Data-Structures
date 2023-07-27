# Day 2:
# Question: Given a string, write a function to count the number of vowels (a, e, i, o, u) in the string.
# Example:
# Input: "programming"
# Output: 3

def vowels(word):
    count = 0
    for letter in word:
        if((letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u')):
            count+=1
    return count

print(vowels('programming'))
