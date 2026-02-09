#enumerate with list values
# enumerate() is a built
fruits = ["orange", "Cherry", "Kiwi"]
for index, fruits in enumerate(fruits):
    print(index, fruits)

#Enumerate with start value changed
for index,fruit in enumerate(fruits, start=1):
    print(index, fruit)

#enumerate with strings
word = "python"
for i, ch in enumerate(word , start = 2):
    print(i, ch)

#enumerate with tuples
fruits = ("orange", "Cherry", "Kiwi")
for index,fruit in enumerate(fruits):
    print(index, fruit)

# real time scenario

test_cases = ["Login", "Signup", "Checkout"]
for case_no, test in enumerate(test_cases, start=1):
    print(f"Executing Testcase {case_no}: {test}")

#accessing of the enumerate values
a = ['God', 'is', 'Great']
b= enumerate(a)
nxt_val = next(b)
print(nxt_val)
print(nxt_val)

#duplicate detection using enumerate

characters = ["Krillin", "Goku", "Gohan", "Piccolo",
              "Krillin", "Goku", "Vegeta", "Piccolo",
              "Piccolo", "Goku", "Vegeta", "Goku", "picolo"]

character_map = {character: [] for character in set(characters)}

for index, character in enumerate(characters):
    character_map[character].append(index)

print(character_map)

a = ['God', 'is', 'Great']
b = enumerate(a)

next(b)
print(next(b)[1])
print(next(b)[1])
