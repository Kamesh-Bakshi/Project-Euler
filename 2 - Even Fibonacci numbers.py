import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a1 = 1
    a2 = 2
    suum = 2
    for i in range(3,n):
        a3 = a1+a2
        a1 = a2
        a2 = a3
        if a3 > n:
            break
        if a3%2 == 0:
            suum += a3
    print(suum)
