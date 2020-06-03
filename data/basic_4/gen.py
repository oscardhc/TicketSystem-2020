
import os

with open("../in.txt", "r") as f:
    idx = 1
    arr = f.read().split('\n')

    o = open('1.in', 'w')
    for l in arr:
        print(l, file=o)
        if l == 'exit':
            o.close()
            idx += 1
            o = open('%d.in' % idx, 'w')
            

with open("../out.txt", "r") as f:
    idx = 1
    arr = f.read().split('\n')

    o = open('1.out', 'w')
    for l in arr:
        print(l, file=o)
        if l == 'bye':
            o.close()
            idx += 1
            o = open('%d.out' % idx, 'w')

print(idx - 1)
os.system('rm %d.in; rm %d.out' % (idx, idx))
os.system('cp ../out.txt ./; cp ../in.txt ./')
