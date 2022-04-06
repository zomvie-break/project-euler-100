#!/usr/bin/env python3

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def action_evens(n):
    return n/2

def action_odds(n):
    return n*3+1

def check_finish(n):
    if n == 1:
        return True
    return False

longest_chain = []              # variable to store the longest chain.
for n in range(10**6, 0, -1):   # for loop, starting from 1,000,000, ending in 1.
    current_chain = []
    while not check_finish(n):
        current_chain.append(n)
        if is_even(n):
            n = action_evens(n)
        else:
            n = action_odds(n)
        current_chain.append(n)

    # if the current chain is longer than the longest_chain, change it.
    if len(current_chain) > len(longest_chain):
        longest_chain = current_chain
        print(f'longest chain starts with #{longest_chain[0]} and has {len(longest_chain)} items')

