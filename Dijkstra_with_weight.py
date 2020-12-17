def way(b):
    pt = []
    while b != -1:
        pt.append(b + 1)
        b = p[b]
    return pt[::-1]


inf = 10000000000000
a = []
st = [int(i) for i in input().split()]
n = 0
while len(st) != 2:
    n = max(n, st[0], st[1])
    a.append(st)
    st = [int(i) for i in input().split()]

start = st[0] - 1
end = st[1] - 1
g = [[] for _ in range(n)]

for st in a:
    g[st[0] - 1].append((st[1] - 1, st[2]))
    g[st[1] - 1].append((st[0] - 1, st[2]))


d = [inf for i in range(n)]
p = [-1 for i in range(n)]

d[start] = 0


u = [0 for i in range(n)]
for i in range(n):
    v = -1
    for j in range(n):
        if not u[j] and (v == -1 or d[j] < d[v]):
            v = j
    if d[v] == inf:
        break
    u[v] = 1
    for j in range(len(g[v])):
        to = g[v][j][0]
        ln = g[v][j][1]
        if d[v] + ln < d[to]:
            d[to] = d[v] + ln
            p[to] = v

print(*way(end), sep=', ')
