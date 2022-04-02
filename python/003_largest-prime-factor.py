#!/usr/bin/env python3

def factors(n):
    # set() removes the duplicates from the list
    # reduce(fun,seq) function is used to apply a particular function passed in its argument
    # to all of the list elements mentioned in the sequence passed along.
    # list.__add__ adds the elements in the list 'x' to the list 'y', similar to append.
    # x is an list holding two factores, i and n//i.
    y = []
    for i in range(1, int(n**0.5) +1 ):

        if n % i == 0:
           x = [i, n//i]
           y = y.__add__(x)
    return set(y)

def isprime(n):

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

results = factors(600851475143)

primes = []
for result in results:
    if isprime(result):
        primes.append(result)

print(max(primes))
