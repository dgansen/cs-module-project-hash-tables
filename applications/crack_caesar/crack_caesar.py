# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

lets = {}
with open('ciphertext.txt') as f:
    for char in f.read():
        if not char.isalpha():
            continue
        if char not in lets:
            lets[char] = 0
        lets[char] += 1

sor = sorted(lets.items(), key=lambda x: x[1], reverse=True)
key_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
key = {s[0]:k for s,k in zip(sor,key_list)}
uncrypted = ''

with open('ciphertext.txt') as f:
    for char in f.read():
        if char in key:
            char = key[char]
        
        uncrypted += char

print(uncrypted)