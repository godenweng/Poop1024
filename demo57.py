data = [[1,2,3,-4,5],
        [6,7,8,9,10],
        [1,3,5,7,9],
        [2,-4,6,8,10]]
print("======= break =======")
for row in data:
    sum = 0
    for col in row:
        if col < 0:
            print('got an outlier %d' % col)
            break
        else:
            sum += col
    else:
        print('row sum =%d' %sum)

print("=======continue =======")
for row2 in data:
    sum2 = 0
    for col2 in row2:
        if col2 < 0:
            print('got an outlier %d' % col2)
            continue
        sum2 += col2
    else:
        print('row sum2 =%d' %sum2)