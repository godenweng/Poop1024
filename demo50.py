def judge(inputScore):
    return 'good' if inputScore >= 80 else 'bad'

score = 80
x1 = judge(score)
print('%d is %s' % (score,x1))

score = 60
x2 = judge(score)
print('%d is %s' % (score,x2))

def judge2(inputScore):
    return ('bad','good')[inputScore >= 80]

score2 = 80
x1 = judge2(score2)
print('[2]%d is %s' % (score2,x1))

score2 = 60
x2 = judge2(score2)
print('[2]%d is %s' % (score2,x2))
