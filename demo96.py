PATH = 'data/python_introduction'
PATH_WRITE1 = 'data/clone1'
PATH_WRITE2 = 'data/clone2'

file1 = open(PATH, encoding='UTF8')
print(type(file1))
data1 = file1.read()
print(type(data1))
file1.close()
print(data1)

with open(PATH, encoding='UTF8') as file2:
    print(type(file2))
    data2 = file2.read()
print(type(data2))
print(data2)

file3 = open(PATH_WRITE1, 'w', encoding='UTF8')
file3.write(data1)
file3.close()

with open(PATH_WRITE2,'w',encoding='UTF8') as file4:
    file4.write(data2)