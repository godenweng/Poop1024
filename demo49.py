A = True
B = False
print(A and A, A and B, B and A ,B and B, not A, not B)
print(A or B,B or A , B or B)
print("========")
date =[True,False,'hi','中文',500,3.14]
for d in date:
    print("A and d --->",A and d)
print("========")

for d in date:
    print("B or d --->", B or d)
print("========")