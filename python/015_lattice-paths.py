#!/usr/bin/env python3

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def get_convinations(gridsize):
    # generally speaking, you can use the binomial coefficient: 'n choose k'. That is
    # '(two times the grid size) choose (the gridsize)'
    return factorial(gridsize*2)/(factorial(gridsize)**2)

# For the routes that can be taken in a grid of size 'm', there are '2m' steps from start to finish.
# E.g. Consider a 2x2 matriz, where the only possible moves are to the right (R) and down (D).
#   So the steps look like this: (R, R, D, D) or (D, R, D, R).
#   In this case and similar ones, exactly half of the steps must be 'R' and the other half must
#   be 'D'.
#
#   As such, we can use the binomial coeficient: n! / (n! * (n-k)!) where 'n' is the number of steps (i.e. '2m')
#   and 'k' is the number of steps that are 'R' or 'D' (i.e. half the number of steps, or 'm')

print(get_convinations(20))
