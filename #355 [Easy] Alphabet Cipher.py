from string import ascii_lowercase as abc
import itertools


def resultchar(i, j):
    s = abc.index(j) + abc.index(i)
    return abc[s - 26] if s > 25 else abc[s]


codeword, message = input(
    'Please enter the codeword and your message: ').split()
codeword = itertools.cycle(codeword)
codephrase = [resultchar(i, next(codeword)) for i in message]

print(f'Your codephrase is: {"".join(codephrase)}')
