import sys
try:
    while True:
        line1 = sys.stdin.readline().strip()
        if line1 == '':
            break
        a, b = line1.split()
        print(a, b)
except:
    pass

