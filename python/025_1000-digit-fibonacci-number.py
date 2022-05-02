#!/usr/bin/env python3

def run():
    term = 0
    fibonacci_n_one = 1         # store F(n-1)
    fibonacci_n_two = 1         # store F(n-2)
    fibonacci_now = 1           # store F(n)

    # while loop that stops when fibonacci_now is greater than 1000 digits
    while len(str(fibonacci_now)) < 1000:

        if term == 0:
            fibonacci_now = 1
        elif term ==1:
            fibonacci_n_one = fibonacci_now
            fibonacci_now = 1
        else:
            fibonacci_n_two = fibonacci_n_one
            fibonacci_n_one = fibonacci_now
            fibonacci_now = fibonacci_n_one + fibonacci_n_two

        # add one to the current term
        term += 1
    print(f'term: {term}\tfibo: {fibonacci_now}')

if __name__ == "__main__":
    run()
