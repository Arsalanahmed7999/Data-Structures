# Question: Write a function that takes two strings as input and returns True if one string is an anagram of the other, otherwise returns False.
# Example:
# Input: "listen", "silent"
# Output: True

def anagram(string1, string2):
    l1 = list(string1)
    l2 = list(string2)
    l1 = sorted(l1)
    l2 = sorted(l2)
    str1 = "".join(l1)
    str2 = "".join(l2)
    return str1.lower() == str2.lower()


a = anagram('listen', 'silent')
b = anagram('listn', 'silent')
print(a)
print(b)