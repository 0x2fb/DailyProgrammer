cypher = {' ||_ _ ||': '0', '       ||': '1', '  |___ | ': '2', '   ___ ||': '3', ' |  _  ||': '4',
          ' | ___  |': '5', ' ||___  |': '6', '   _   ||': '7', ' ||___ ||': '8', ' | ___ ||': '9'}


def decipher(s):
    blocks = [''.join(i) for i in zip(*s.split('\n'))]
    comp = [''.join([blocks[i], blocks[i + 1], blocks[i + 2]])
            for i in range(0, len(blocks), 3)]
    result = ''.join([cypher[i] for i in comp])
    print(result)


decipher('''    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|''')

decipher('''    _  _  _  _  _  _  _  _ 
|_| _| _||_|| ||_ |_| _||_ 
  | _| _||_||_| _||_||_  _|''')

decipher(''' _  _  _  _  _  _  _  _  _ 
|_  _||_ |_| _|  ||_ | ||_|
 _||_ |_||_| _|  ||_||_||_|''')

decipher(''' _  _        _  _  _  _  _ 
|_||_ |_|  || ||_ |_ |_| _|
 _| _|  |  ||_| _| _| _||_ ''')
