# Question: Write a function that takes a string as input and returns True if it is a palindrome (reads the same backward as forward), otherwise returns False.
# Example:
# Input: "racecar"
# Output: True

def palindrome(word):
    if(word == word[::-1]):
        return True
    return False

a = palindrome("racecar")
b = palindrome("abc")
print(a)
print(b)