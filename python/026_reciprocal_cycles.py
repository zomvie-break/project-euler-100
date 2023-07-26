#!/usr/bin/env python3

def run():
    scores = {}
    highest = 0
    len_highest = 0
    for i in range(1,1000): # go from 1 to 999
        divisor = i
        dividend = 1

        # array to store the quotients of the divisions.
        # The len of this array will for each divisor will determine
        # the longest reciprocal cycle.
        quotients = []

        # array to store the remainders of the division.
        # The last remainder times 10 will be the next dividend.
        remainders = []

        # first run, this is 1. except for 1/1 which is 0.
        remainders.append(dividend % divisor)

        while remainders[-1] != 0:
            # new dividend, i.e. last remainder times 10
            dividend = remainders[-1] * 10
            quotients.append(dividend//divisor)
            new_remainder = dividend % divisor

            # if the new remainder is already in the remainders, that means the
            # quotients will start repeating themselves.
            if new_remainder in remainders:
                break
            remainders.append(new_remainder)


        # print(f'divisor: {divisor}\tdividend: {dividend}\tquotients: {quotients}\tremainders: {remainders}')
        scores[divisor] = len(quotients)

    # sorted_scores will return a list of tupples in the form (divisor, len(quotients))
    sorted_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)
    print(f'sorted_scores: {sorted_scores[0:10]}')

run()
# the answer is d  = 983, where the reciprocal cycle has a legth of 982 numbers!
