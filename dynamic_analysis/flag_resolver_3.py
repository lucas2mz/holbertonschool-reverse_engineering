import struct

# valores GDB
values = [
    0x08070523,
    0x04172d03,
    0x5a4e1114,
    0x05354056,
    0x0211090e,
    0x033b4c31,
    0x340d0704,
    0x11253032,
    0x13202700,
    0x5a02033b
]

last = 0x4f5e

encoded = b''

for v in values:
    encoded += struct.pack("<I", v)

encoded += struct.pack("<H", last)

encoded = encoded.ljust(0x80, b"\x00")

# key
key = b"kjkjf_ckzj9274jdlfdvn-dpakkk__AhfNNtdsp592"

decoded = bytearray()

for i in range(len(encoded)):
    decoded.append(encoded[i] ^ key[i % len(key)])

flag = decoded.split(b"\x00")[0]

print(flag)
print(flag.decode(errors="ignore"))