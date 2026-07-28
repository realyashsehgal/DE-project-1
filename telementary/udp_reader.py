import struct

data = b'\x2A\x01'

number = struct.unpack('<H',data)

print(number)