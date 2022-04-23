#!/usr/bin/env python3

def get_divisors(n):
    '''function that returns the proper divisors of a number (i.e. not including the number itself)'''
    divisors = []
    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            divisors = divisors.__add__([i, n/i])
    # remove n from the divisors
    if n in divisors:
        divisors.remove(n)
    # cast the list to set and then back to list to remove duplicates (e.g. 4, 9, 16, 25. These are perfect squares)
    return list(set(divisors))

def sum_list(nlist):
    '''return the sum of all the elements in the list'''
    return sum(nlist)

def abundant_divisor(n):
    ''' function that classifies n according to its divisors (perfect, abundant, non-abundant)'''
    divisors = get_divisors(n)
    divisors = sum_list(divisors)

    # only the 'abundant' variable is relevant for this problem
    if divisors > n:
        return n
    else:
        return 0

def get_all_sums(alist, max_val):
    '''calculates all the sums of two numbers of the 'alist' and adds them to an array as long as the sum is not bigger  '''
    sums = [0] * max_val
    for i in range(len(alist)):
        for j in range(i, len(alist)):
            temp = alist[i] + alist[j]
            # since we are only interested in numbers smaller than 'max_val'
            # we do not append any value larger than that (it would raise an error)
            if temp < max_val:
                sums[temp] = temp

    return sums

def run():
    # list that stores abundant divisors
    abundant = []
    # it stores the sum of all the numbers in the range 1..28122
    all_numbers = 0

    # calculates all abundant divisors of the range 1..28122
    for i in range(1, 28123):
        temp = abundant_divisor(i)
        if temp:
            abundant.append(temp)
        all_numbers += i

    sums = get_all_sums(abundant, 28123)

    result = all_numbers - sum(sums)
    print(f'the answer is: {result}')


if __name__ == '__main__':
    run()
