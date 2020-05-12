from collections import deque


def bfs(s):
    q = deque()
    q.append(s)
    d[s] = 0
    while len(q):
        v = q.popleft()
        for to in g[v]:
            if d[to] == inf:
                d[to] = d[v] + 1
                p[to] = v
                q.append(to)


def path(f):
    pt = []
    while f != -1:
        pt.append(f + 1)
        f = p[f]
    return pt[::-1]


inf = 1000000000
n, m = map(int, input().split())
g = [list() for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
d = [inf] * n
p = [-1] * n

s, f = map(int, input().split())
s -= 1
f -= 1
bfs(s)
print(d[f])
print(*path(f))