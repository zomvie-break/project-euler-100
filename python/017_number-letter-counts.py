#!/home/victor/documents/project-euler/python/venv/bin/python3

from num2words import num2words

sum = 0
for i in range(1,1001):
    word = num2words(i).replace(' ', '').replace('-','')
    sum+=len(word)

print(sum)
