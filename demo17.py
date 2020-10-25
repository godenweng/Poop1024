from distutils.util import strtobool

strings = ['TRUE','true','True','FALSE','false','False','T','F']

for s in strings:
    int1 = strtobool(s)
    print(type(int1),type(bool(int1)))
    print("{} will become {}".format(s, bool(int1)))