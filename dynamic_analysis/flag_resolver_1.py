def ror(x, n):
    return ((x >> n) | (x << (8 - n))) & 0xff

def prng(seed):
    seed = (seed * 0x41C64E6D + 0x3039) & 0x7fffffff
    return (seed >> 16) & 0xff, seed

target = []

def add_qword(val):
    for i in range(8):
        target.append((val >> (8*i)) & 0xff)

def add_dword(val):
    for i in range(4):
        target.append((val >> (8*i)) & 0xff)

def add_word(val):
    for i in range(2):
        target.append((val >> (8*i)) & 0xff)

def add_byte(val):
    target.append(val)

add_qword(0x4ef0a378ebed0049)
add_qword(0x459656f85013994a)
add_qword(0x0dabf8aa60e91585)
add_qword(0xce48306873d32868)
add_qword(0x7323a57a29d08d6d)
add_dword(0xe1ea56d8)
add_word(0x605f)
add_byte(0x5a)

assert len(target) == 47

seed = 0x3039
result = []

for b in target:
    rand, seed = prng(seed)

    x = (b + 0x5b) & 0xff
    x = ror(x, 3)
    x ^= rand

    result.append(x)

flag = bytes(result)

print("FLAG:", flag.decode(errors="ignore"))