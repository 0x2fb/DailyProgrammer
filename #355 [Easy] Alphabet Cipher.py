from string import ascii_lowercase as abc
import itertools


def encrypt(codeword, message):
    def resultchar(i, j):
        s = abc.index(j) + abc.index(i)
        return abc[s - 26] if s > 25 else abc[s]
    codeword = itertools.cycle(codeword)
    codephrase = [resultchar(i, next(codeword)) for i in message]
    return "".join(codephrase)


def decrypt(codeword, message):
    def resultchar(i, j):
        s = abc.index(i) - abc.index(j)
        return abc[s + 26] if s < 0 else abc[s]
    codeword = itertools.cycle(codeword)
    codephrase = [resultchar(i, next(codeword)) for i in message]
    return "".join(codephrase)


print(encrypt('snitch', 'thepackagehasbeendelivered'))
print(encrypt('bond', 'theredfoxtrotsquietlyatmidnight'))
print(encrypt('train', 'murderontheorientexpress'))
print(encrypt('garden', 'themolessnuckintothegardenlastnight'))

print(decrypt('cloak', 'klatrgafedvtssdwywcyty'))
print(decrypt('python', 'pjphmfamhrcaifxifvvfmzwqtmyswst'))
print(decrypt('moore', 'rcfpsgfspiecbcc'))
