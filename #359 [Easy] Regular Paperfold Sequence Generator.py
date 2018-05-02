def paperfold(cycle):

    def curve(sequence):
        num = '1'
        flag = True
        for i in sequence:
            if flag:
                num = num + i + '0'
                flag = False
            else:
                num = num + i + '1'
                flag = True
        return num
    sequence = '1'
    for _ in range(cycle):
        sequence = curve(sequence)
    return sequence


print(paperfold(8))

'''
# Solution by '110100100_Blaze_It':

arr = [1]
for i in range(8):
    arr = arr + [1] + [bit ^ 1 for bit in arr[::-1]]

print(''.join([str(bit) for bit in arr]))
# Every time the sequence adds bits the old sequence is put to the left half and 
# a 'bitwise exclusive OR' sequence is put to the right half separated by a 1
'''
