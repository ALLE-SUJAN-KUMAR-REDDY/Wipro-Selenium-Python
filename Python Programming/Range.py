a = range(0,5)
print(a[1])
print(a[3])

a1 = range(2,5)
print(a1[1])

a = range(2,5)
for i in a:
    print(i)

a = range(2,15,-3)
for i in a:
    print(i)


#Scenario : Allow 3 login attempts
for attempt in range(3):
    pin = input("Enter the pin:")
    if pin == "1234":
        print("Access granted")
        break
    else:
        print("Account locked")

#Scenario : Apply discount based on the position (index) of the item
prices = [100,200, 300,400]
for i in range(len(prices)):
    if i % 2 == 0:
        print("Discount applied on item {1}")

#Scenario : simulate polling every second for 10 seconds

import time
for second in range(10):
    print("Checking the status at {second} sec")
    time.sleep(1)

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