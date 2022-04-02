#!/usr/bin/env python3

def chech_squares(a,b,c):
    return a**2 + b**2 == c**2

def check_sum(a,b,c,n):
    return a + b + c == n


def check_values(a,b,c):
    return a < b and b < c


triplets = [['a', 'b', 'c']]
n = 1000

for a in range(1,n):
    for b in range(1,n):
        for c in range(1,n):
            if not check_values(a,b,c):
                # print(f'a: {a} b: {b} c: {c}')
                continue
            if chech_squares(a,b,c):
                triplets.append([a,b,c])
                # print(f'a: {a}\tb: {b}\tc: {c}\ttriples found: {len(triplets)}')
                if check_sum(a,b,c, n):
                    print(f'a: {a}\tb: {b}\tc: {c}\tn: {n}')

print(f'found {len(triplets)-1}')
# print(triplets)
