# match - match the exact sequence

import re

# o/p  match object - matched sequence and span () - start and end index

text ="123Hello World"
result = re.match("Hello",text)
print(result)

# using pattern

test_str = "12356677abcghhhjhjabcABC"
pattern = re.compile("123")

# re.finditer() finds all non-overlapping matches of a pattern in a string and
# returns an iterator of match objects (non a list)
matches = pattern.finditer(test_str)

for match in matches:
    print(match)

# search operations searches the entire string
# returns the first occurrence
result = "python is powerful math powerful"
result = re.search("powerful",text)
print(result)

# search - - search is entire string - find the occurrence
# raw string for including the special character

a = r"\tHello"
print(a)

# match() - Determine if the RE matches at the beginning of the string.
# search() - Scan through a string, looking for any location where this RE matches.
# finditer() - Find all substring where the RE matches, and returns them as an iterator
# findall() - Find all the substring where the re matches and returns a list

# findall()

my_string ="abc123ABC123abc"
pattern = re.compile(r'123')
matches = pattern.findall(my_string)

for match in matches:
    print(match)

# Methods on match

# group() - Return the string matched by the RE
# start() : Return the starting position of the match
# end() : Return the ending position of the match
# span() :Return a tuple containing the (start, end) positions of the match

test_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print(match.group()) # return the substring that was matched by the RE

# special characters
# meta characters
# regular expressions

# Pattern Meaning

# abc Matches exact text
# [abc] a or b or c
# [a-z] lowercase letters
# [0-9] digits
# 'a b'
# Any single character

# abc Matches  exact text
# match exact "abc" wherever it is appearing
text = "I like abc and abcde"
result = re.findall("abc", text)
print(result)

# [abc] a or b or c - matches any one of the character
import re

text = "abc xyz bac"
result = re.findall("[abc]", text)
print(result)


# [a-z] lowercase letters
text = "I Like abc and ABCGHJHJH"
result = re.findall("[a-z]", text)
print(result)

#[0-9] digits
text = "I Like abc and 123455ABCGHJHJH"
result = re.findall("[0-9]", text)
print(result)

# 'a b'
text = "cat bat rat mat"
result = re.findall("cat|bat", text)
print(result)
# Matches either "cat" OR "bat"

# any single character
text = "cat bat rat bob"
result = re.findall("c.t", text)
print(result)

# special characters

'''
Special sequences begin with a backslash \.
Sequence    Meaning    Example
\d  Digit (0–9)    \d\d
\D  Non-digit  \D
\w  Word char (a-z, A-Z, 0-9, _)   \w+
\W  Non-word char  \W
\s  Whitespace \s
\S  Non-whitespace \S
\b  Word boundary  \bcat\b
\B  Not a word boundary    \Bcat
'''

#\d Digit (0-9) \d\d
print(re.findall(r"\d", "Order 123 costs 450"))

# \D Non-digit
print(re.findall(r"\D", "Order 123 costs 450"))

# \W Non-word char \W
#Matches anything that is Not a word character
text = "Hello@123!"
result = re.findall(r"\w", text)
print(result)

# \s Whitespace spaces, tabs and newline

text ="Hello World\nPython"
result = re.findall(r"\s", text)
print(result)

# \S Non-whitespace \S - Matches anything that is NOT space
text = "Hi There"
result = re.findall(r"\S", text)
print(result)

#\b Word boundary - Matches position at start or end of a word.
text = "cat scatter catalog"
result = re.findall(r"\bcat\b", text)
print(result)

# Matches only full word "cat"

#\B Not a word boundary \Bcat - Matches when pattern is NOT at word boundary.
text ="cat scatter catalog"
result = re.findall(r"cat\B", text)
print(result)

"""
Meta - characters have special meaning in regex.
Meta - character Meaning
.Any character
^ Start of string $   End of string
*0 or more +   1 or more ?   0 or 1 {n} Exactly n times {n, } n or more {n, m}
Between n and m []
Character set ()
Grouping
"""


#^ Start of string
text = "easy Python"
print(re.findall(r"^Python", text))

#$ End of the string
text = "Python is easy"
print(re.findall(r"easy$", text))

#* 0 or more
text = "ab abb abbb a n"
print(re.findall(r"ab*", text))

#+ 1 or more
text = "ab abb abbb a"
print(re.findall(r"ab+", text))

#? 0 or 1
text = "color colour colr"
print(re.findall(r"colou?r", text))

#{n} Exactly n times
text = "111 22 3333 68777"
print(re.findall(r"\d{3}",text))

#{n,} n or more
text = "1 22 333 4444"
print(re.findall(r"\d{3}", text))

#{n,m} Between n and m
text = "1 22 333 4444"
print(re.findall(r"\d{2,3}", text))

# [] character set

text = "apple banana cat"
print(re.findall(r"[abc]", text))

#() Grouping
text = "2026-02-11"
result = re.findall(r"(\d{4})-(\d{2})-(\d{2})", text)
print(result)


# Regular expression modifiers

'''
Modifier    Short  Purpose
re.IGNORECASE   re.I   Case-insensitive matching
re.MULTILINE    re.M   ^ and $ match each line
re.DOTALL   re.S   . matches newline
re.VERBOSE  re.X   Write readable regex with comments
re.ASCII    re.A   ASCII-only matching
re.DEBUG    —  Debug pattern
'''

#re.IGNORECASE re.I CASE-insenstive matching
text ="Python"
print(re.search("Python", text, re.I))

#DOTALL re.S matches newline
text = "Hello\nWorld"
print(re.search("Hello.*World", text, re.S))

#re.MULTILINE re.M  ^ and $ matches eachline
text = "Hello\nPython"
print(re.findall("^Python", text, re.M))

#re.VERBOSE re.X Write readable regex with comments - make it more readable
import re
pattern = re.compile(r"""7879hbgjksdgdskl..%^^&*&89""", re.X)
print(pattern)

# re.ASCII re.A ASCII-only matching
print(re.findall(r"\w+", text, re.A))

# re.DEBUG - Debug pattern
pattern = re.compile(r"""
7879hbgjklksdgdskl..%^^&*&89""", re.DEBUG)
print(pattern)

# assertions - valdating the output or checking certain condition

"""
^ -> Start of string
$ -> End of string
\b -> Word boundary
\B -> Not word boundary
(?=...) -> Positive Lookahead
(!...) -> Negative Lookahead
(?<=...) -> Positive Lookahead
(?<!...) -> Negative Lookahead
"""

import re

text = "Python is easy"
print(re.findall(r"Python", text))

text = "Python is easy"
print((re.findall(r"easy$", text)))

text ="cat scatter catalog"
print(re.findall(r"\bcat\b", text))

text ="cat scatter catalog"
print(re.findall(r"cat\B", text))

#(?#...) -> Positive Lookahead = match only if followed by something
text = "User1 admin2 test"
print(re.findall(r"\w+(?=\d)", text))

#(?!...) -> Negative Lookahead
text = "user1 admin test2"
print(re.findall(r"\w+(?!\d)", text))

#(?<=...) -> Positive Lookahead - match only if preceeded by something
text = "Price ₹500"
print(re.findall(r"(?<=₹)\d+", text))

#(?<!...) -> Negative Lookahead
text = "500 ₹300"
print(re.findall(r"(?<!₹)\d+", text))




