#!/usr/bin/env python3

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

# this is the example given
x = range(1,11)
target = 2520
for i in x:
    print(target/i)

# this is what I'm asked to do
def check_divisible(n, divisors):
    # goes throuh each element in the divisors list and tries to divede n.
    for divisor in divisors:
        # if the remainder is not cero for any divisor, then the number is
        # not the smallest multiple
        if n % divisor != 0:
            return False
    # If the code reaches this point, it means it found the smallest multiple
    print(f'{n} is the smallest multiple of 1..20')
    return True

    
# creates an list from 1 to 20.
x = range(1,21)
# initialize i to 20
i = 20
while not check_divisible(i, x):
    # adds 2 to i, since the number has to end in 2,4,6,8,0 in order
    # to be divisible by 2.
    i += 2
