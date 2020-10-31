import  sys

text = ''

while True:
    c = sys.stdin.read(1)
    text += c
    if c == '\n':
        break

print("resule={}".format(text))