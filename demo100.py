FILES = ['data/image1.jpg','data/image2.png','data/image3.jpg','data/image4.png',
         'data/image1.rar','data/image2.rar']


for file in FILES:
    print("filename={}".format(file))
    with open(file, 'rb') as f:
        index = 1
        #byte = f.read(1)
        while (byte := f.read(1)) != "" and index < 9:
            x = int.from_bytes(byte,byteorder= 'little')
            print("%d,%4s" % (index, str(hex(x))))
            #byte = f.read(1)
            index += 1