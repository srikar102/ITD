# # Case conversion
# text = "Hello World"
# print(text.lower())           # hello world
# print(text.upper())           # HELLO WORLD
# print(text.capitalize())      # Hello world
# print(text.title())           # Hello World

# # Searching and replacing
# print(text.find("World"))     # 6
# print(text.replace("World", "Python"))  # Hello Python
# print(text.startswith("Hello"))  # True
# print(text.endswith("World"))    # True

# # Whitespace handling
# text2 = "  Python  "
# print(text2.strip())          # Python
# print(text2.lstrip())         # Python  
# print(text2.rstrip())         # Python

# # Splitting and joining
# csv = "apple,banana,orange"
# fruits = csv.split(",")      # ['apple', 'banana', 'orange']
# print(" | ".join(fruits))    # apple | banana | orange

# # Checking content
# print("123".isdigit())        # True
# print("abc".isalpha())        # True
# print("abc123".isalnum())     # True

# # String formatting
# name = "Alice"
# age = 25
# print(f"{name} is {age} years old")  # Alice is 25 years old
# print("{}:{}".format("user", "admin"))  # user:admin
# print(len("Hello"))           # 5


name = "DevOps/Python/datatypes.py"
print(name[:]) #prints the full string
print(name[0:6]) #prints 'DevOps'
print(name[::-1]) #prints the string in reverse

# Interview Questions on Strings

# 1. Reverse a string
text = "hello"
print(text[::-1])  # olleh

# 2. Check if string is palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # True

# 3. Count character occurrences
text = "hello world"
print(text.count("l"))  # 3

# 4. Remove duplicates and preserve order
def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

print(remove_duplicates("aabbcc"))  # abc

# 5. Check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(are_anagrams("listen", "silent"))  # True

# 6. String compression
def compress_string(s):
    compressed = []
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            compressed.append(s[i] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    return "".join(compressed)

print(compress_string("aabbcc"))  # a2b2c2

# 7. Longest substring without repeating characters
def longest_substring(s):
    char_map = {}
    max_length = 0
    start = 0
    for end in range(len(s)):
        if s[end] in char_map:
            start = max(start, char_map[s[end]] + 1)
        char_map[s[end]] = end
        max_length = max(max_length, end - start + 1)
    return max_length

print(longest_substring("abcabcbb"))  # 3