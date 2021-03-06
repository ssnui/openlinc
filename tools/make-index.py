import os
import os.path
import sys

MAX_INDEX_SIZE = 2048

def find_index(name, ext, ext2):
    text_file = open(name + ext, 'rb')
    text = text_file.read()
    text_file.close()

    idx = ''.join(['%02x' % ord(c) for c in open(name + ext2, 'rb').read()])

    count = len(idx) / 16

    c = 0
    while c < count:
        hoffset = idx[c*16:c*16+8]
        hvalue = idx[c*16+8:c*16+16]

        offset = int(hoffset[2:4] + hoffset[0:2], 16)
        value = int(hvalue[2:4] + hvalue[0:2], 16)

        key = text[offset:offset+64].split('~',2)[1]

        if value > MAX_INDEX_SIZE:
            raise Exception('value out of range -- increase MAX_INDEX_SIZE to %s' % value)

        index[value] = key

        c = c + 1

index = {}
for x in range(0, MAX_INDEX_SIZE):
    index[x] = 'x%s' % x

files = os.listdir('.')
for filename in files:
    if filename[-1:] == '#':
        name, ext2 = os.path.splitext(filename)
        if ext2 == '.ht#':
            ext = '.htm'
        elif ext2 == '.xm#':
            ext = '.xml'
        else:
            raise Exception('unexpected extension %s' % ext2)

        find_index(name, ext, ext2)

s = ''
for k in range(0, MAX_INDEX_SIZE):
    s += index[k] + '|'

print s[:-1]


