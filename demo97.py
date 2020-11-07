OUTPUT_FILE1 = 'data/demo97'
file1 = open(OUTPUT_FILE1,'w')
linesToWrite = ['first line\n','second line\n','apple\n','banana\n','cookie\n']
file1.writelines(linesToWrite)
file1.close()

for i in range(10):
    file2 =  open(OUTPUT_FILE1,'a')
    nextLine = ['addsometiong \n']
    file2.writelines(nextLine)
    file2.close()