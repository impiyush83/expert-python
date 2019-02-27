"""

list.sort() when you want to mutate the list.

sorted() when you want a new sorted object back.

"""

l1 = [1, 4, 6, 2, 3]
l1.sort()
print(l1)  # l1 is permanatly mutated to sorted list

l1 = [1, 4, 6, 2, 3]
print(sorted(l1))  # l1's sorted list is returned
print(l1)  # original list is obtained back
