
# Zero Width Space Page 

When you don't see the content of file but it's extension is right . 

1. Use hexeditor and see the magic bytes of file 
2. Analyzie magic bytes
3. Then , write code  according to magic bytes


from Crypto.Util.number import *

with open('zwsp.txt', 'rb') as f:
    data = f.read()

i = 0
curr = []

bin_string = ''

for char in data:
    if char not in b'Pretty empty over here':
        i += 1
        curr.append(char)
        if i % 3 == 0:
            i = 0
            print(curr)

            if curr[-1] == 139:
                bin_string += '0'
            else:
                bin_string += '1'

            curr = []

print(bin_string)
print(int(bin_string, 2))
print(long_to_bytes(int(bin_string, 2)))
