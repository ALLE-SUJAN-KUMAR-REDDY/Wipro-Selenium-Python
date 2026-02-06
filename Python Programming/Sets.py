#sets do not allow duplicate elements it contains only unique data
#unordered collection

# create a student_id set integer type
stu_id = {112, 113,114, 115, 115, 116, 8, 10, 45}
print(stu_id)


#crete a string type set
letters = {'a', 'b', 'c', 'd', 'e'}
print(letters)

#create a mixed set
mixed_set = {"Hello", 1,-7,8,9}
print(mixed_set)

#create a empty set
empty_set = set()

# Sample sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

#Adds a single element add()
A.add(10)
print(A)

#clear() Removes all elements
A.clear()
print(A)   # set()

#copy() Creates a copy of a set
C = B.copy()
print(C)

#difference() (-) Elements in A but not in B
print(A.difference(B))
# OR
print(A - B)

#difference_update() (-=) Removes common elements from A
A.difference_update(B)
print(A)

#discard() Removes element (NO error if not present)
B.discard(10)
print(B)

#intersection() (&) Common elements
print(A.intersection(B))
# OR
print(A & B)

#intersection_update() (&=) Keeps only common elements
A.intersection_update(B)
print(A)

#isdisjoint() No common elements?
print(A.isdisjoint(B))  # True or False

#issubset() (<= , <)
print(A.issubset(B))
print(A <= B)   # subset
print(A < B)    # proper subset

#issuperset() (>= , >)
print(B.issuperset(A))
print(B >= A)
print(B > A)

#pop() Removes a random element
A = {10, 20, 30}

A.pop()
print(A)

#remove() Removes element (ERROR if not present)
A = {10, 20, 30}

A.remove(20)
print(A)   # works


#symmetric_difference() (^) Elements NOT common
print(A.symmetric_difference(B))
# OR
print(A ^ B)

#symmetric_difference_update() (^=)
A.symmetric_difference_update(B)
print(A)

#union() (|) Combines both sets
print(A.union(B))
# OR
print(A | B)

#update() (|=) Adds elements of another set
A.update(B)
print(A)

