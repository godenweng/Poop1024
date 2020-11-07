import struct

output_file1 = open("data/demo101.bin", 'wb')
output_file2 = open("data/demo101.ascii", 'w')
for i in range(0, 100):
    print('i=%d, packed as=%s' % (i, repr(struct.pack('i', i))))
    output_file1.write(struct.pack('i', i))
    output_file2.write("%s\n" % str(i))
output_file1.close()
output_file2.close()

input_file1 = open('data/demo101.bin', 'rb')
try:
    block = input_file1.read(400)
    str = ""
    for ch in block:
        str += hex(ch) + " "
    print(str)
    pass
finally:
    input_file1.close()
print(str)
