#!/usr/bin/env python3

from itertools import permutations

# create a itertools.permutations object which stores the permutations of the elements within the list [0,1,2,3,4,5,6,7,8,9]
perm = permutations(range(10))

# cast the object to a list and access its 1,000,000th element.
print(list(perm)[10**6-1])
