#!/usr/bin/env python3

def get_score(name):
    '''
    returns the sum of the values of a string as int ('a' is one, 'b' is two, and 'ab' is three)
    '''
    name = name.lower()
    result = 0
    for char in name:
        # the char 'a' is number 97 by default using ord() so substract 96 for it to be 1.
        result += ord(char) - 96
    return result


def run(filename):
    '''
    reads the file, sorts it, and iterate over the names in the list
    '''
    with open(filename, 'r') as f:
        names = f.readlines()
        # remove trailing spaces, removs " and splits the names at every coma.
        names = names[0].strip().replace("\"", '').split(',')
        names = sorted(names)

        result = 0
        counter = 1
        for i in range(len(names)):
            temp = get_score(names[i])
            prod = temp * (i+1)
            result += prod

    return result


if __name__ == '__main__':
    print(run('/home/victor/documents/project-euler/python/files/p022_names.txt'))
