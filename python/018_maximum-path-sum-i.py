#!/usr/bin/env python

def str_to_lists(string):
    """
    Function to create a list of lists of the string triangle. Each row as a list.
    """
    rows = string.strip().split('\n')
    list_numbers = []
    for row in rows:
        temp = row.split(' ')
        temp = [int(n) for n in temp]
        list_numbers.append(temp)

    return list_numbers

def sum_rows(long_row, short_row):
    """
    This funtion takes two rows, one shorter than the other (by 1), and outputs one row the size of the smallest one.
    This row contains the maximum value for each sum (considering two numbers from the larger row and one for the smaller one)
    """
    new_row = []
    # loop that goes through all the numbers in the shorter row
    # and then compares the two numbers below (in the longer row) and
    # adds the bigger one.
    for i in range(len(short_row)):
        if long_row[i] > long_row[i+1]:
            val = long_row[i] + short_row[i]
            new_row.append(val)
        else:
            val = long_row[i+1] + short_row[i]
            new_row.append(val)
    return new_row

def run(triangle):
    """
    sums all the rows in the triangle, from bottom to top, reducing the dimentions of the triangle and rows by one
    on each iteration.
    """
    # variable to store the end result
    last_row = []
    for i in range(len(triangle),1, -1):
        index = i-1
        # checks if the last_row is empty. If so, initialize it with the last row from the triangle, and one befor it.
        if last_row == []:
            last_row = sum_rows(triangle[index], triangle[index-1])
        else:
            last_row = sum_rows(last_row, triangle[index-1])
    return last_row

triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

triangle = str_to_lists(triangle)

print(run(triangle))
