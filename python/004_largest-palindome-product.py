#!/usr/bin/env python3

def check_palindrome(n):
    '''
    Function used to check if n is a palindrome or not.
    Returns True if it is. Returns False if it isn't.
    '''
    n_string = str(n)
    # this checks if the beginning of the string is the same as the ending.
    # len(n_string)//2+1 is used since there is no point comparing the same element twice.
    for i in range(len(n_string)//2+1):
        # checks if it is NOT a palindrome and exits if it is the case.
        if n_string[i] != n_string[-(i+1)]:
            return False
    # since it did not exit, it means n is a palindrome, return True and exit.
    return True

# dictionary to store the palindromes and its multiplicand and multiplier.
palindromes = {}
#  goes through all three digit numbers and their products.
for i in range(999,99,-1):
    for j in range(999, 99, -1):
        product = i*j
        if check_palindrome(product):
            palindromes[product] = [i,j]

print(f'The biggest palindrome is {max(palindromes.keys())} which is product of {palindromes[max(palindromes.keys())]}')
