scores = [70,60,80,50,90]

def judge1(x):
    if x < 60:
        return 'fail'
    else:
        return  'pass'

for score in scores:
    print("{}-->{}".format(score,judge1(score)))


def judge2(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return  'B'
    elif x >= 70:
        return  'C'
    elif x >= 60:
        return  'D'
    else:
        return 'fail'

for score in scores:
    print("[II]{}-->{}".format(score,judge2(score)))
