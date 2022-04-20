#!/usr/bin/env python3
def get_factors(n):
    '''
    function that returns a list with all the factors of n (excluding n)
    '''
    factors = []

    for i in range(1, int(n**(1/2)+1)):
        if n%i == 0:
            factors = factors.__add__([i, n/i])

    if n in factors:
        # print(f'r: {n}', end=' ')
        factors.remove(n)

    factors = [int(x) for x in factors]
    return factors

def d(n):
    '''
    function that returns the sum of all the factors of n
    '''
    factors = get_factors(n)
    if len(factors) == 0:
        return 0
    else:
        return sum(factors)

def check_amicables(list_numbers):
    '''
    funtion that returns a list of all the amicable pairs as a list
    '''
    # list to store the amicable pairs
    amicables = []
    # loop throughout the list
    for i in range(len(list_numbers)):
        # make sure that the value at index i is not greater than the lenght of the list
        if list_numbers[i] <= len(list_numbers):
            # check if the number at index i has an amicable pair
            # and that it is not itself e.g 6 and 496
            if list_numbers[list_numbers[i]] == i and i != list_numbers[i]:
                amicables.append(i)
    return amicables

def run():
    # a list that stores the sumof the factors of all 10,000 numbers
    all_sums = []
    # for loop, 0..10000 to generate the sums of factors of all wanted numbers
    for i in range(10001):
        factors = get_factors(i)
        temp = sum(factors)
        all_sums.append(temp)

    # look for amicable pairs
    amicables = check_amicables(all_sums)

    return sum(amicables)


if __name__ == '__main__':
    print(run())
