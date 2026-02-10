# 1. Write a regex to check if a string contains only digits.

import re

text = "123456"
print(bool(re.fullmatch(r"\d+", text)))

# 2.Write a pattern to match a 10-digit mobile number.

print(bool(re.fullmatch(r"\d{10}", "9876543210")))

# 3.Find all lowercase letters in a string.

text = "Hello Python"
print(re.findall(r"[a-z]", text))

# 4.Extract all uppercase letters from a sentence.

text = "Hello PYTHON World"
print(re.findall(r"[A-Z]", text))


# 5.Match a string that starts with "Hello".

print(bool(re.match(r"^Hello", "Hello World")))

# 6.Match a string that ends with "world".

print(bool(re.search(r"world$", "Hello world")))

# 7.Find all words separated by spaces.

text = "Python is very easy"
print(re.findall(r"\w+", text))

# 8.Match exactly 5 characters.

print(bool(re.fullmatch(r".{5}", "Hello")))


# 9.Find all occurrences of the word "python" (case-sensitive).

text = "python Python python"
print(re.findall(r"python", text))

# 10.Replace all spaces in a string with underscores.

text = "Python is easy"
result = re.sub(r"\s", "_", text)
print(result)

