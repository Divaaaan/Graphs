def dfs(s):
    global cyc_beg
    global cyc_end
    used[s] = 1
    for to in g[s]:
        if used[to] == 0:
            p[to] = s
            if dfs(to):
                return True
        elif used[to] == 1:
            cyc_beg = to
            cyc_end = s
            return True
    used[s] = 2
    return False
 
def int1(a):
    return int(a) - 1


def path(s, f):
    pt = []
    while f != s:
        pt.append(f + 1)
        f = p[f]
    pt.append(s + 1)
    return pt[::-1]


n, m = map(int, input().split())
g = [[] for i in range(n)]
used = [0] * n
p = [-1] * n
for i in range(m):
    a, b = map(int1, input().split())
    g[a].append(b)
 

cyc_beg = -1
cyc_end = -1
for i in range(n):
    if used[i] == 0:
        if dfs(i):
            break
if cyc_beg == -1:
    print("No cycle")
else:
    print("Cycle")
    print(*path(cyc_beg, cyc_end))
