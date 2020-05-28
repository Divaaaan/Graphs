from math import sqrt

def partRSQ(r):
    it = 0
    sm = 0
    while (it+1) * ln - 1 <= r:
        sm += b[it]
        it += 1
    for i in range(it * ln, r + 1):
        sm += a[i]
    return sm

def RSQ(l, r):
    #return partRSQ(r) - (0 if l == 0 else partRSQ(l - 1))
    if l == 0:
        return partRSQ(r)
    else:
        return partRSQ(r) - partRSQ(l - 1)

def v2RSQ(l, r):
    sm = 0
    while(l <= r):
        if l % ln == 0 and l + ln - 1 <= r:
            sm += b[l // ln]
            l += ln
        else:
            sm += a[l]
            l += 1
    return sm

def v3RSQ(l, r):
    sm = 0
    0, ln, 2 * ln
    while l % ln != 0 and l <= r:
        sm += a[l]
        l += 1
    it = l // ln
    while it * ln + ln - 1 <= r:
        sm += b[it]
        it += 1
    for i in range(max(l, it * ln), r + 1):
        sm += a[i]
    return sm
    
def UPD(i, x):
    b[i // ln] += x - a[i]
    a[i] = x

n = int(input())
a = list(map(int, input().split()))
ln = int(sqrt(n)) + 1
b = [0] * ln
for i in range(n):
    b[i // ln] += a[i]
k = int(input())
for i in range(k):
    q, e = map(int, input().split())
    print(RSQ(q - 1, e - 1), end = ' ')
