from collections import deque

def bfs(i,j,k):
    q = deque()
    q.append([i, j, k])
    d[i][j][k] = 0
    while len(q):
        v = q.popleft()
        for to in step(v[0], v[1]):
            if g[to[0]][to[1]] == 0:
                if d[to[0]][to[1]][v[2]] == 1000000:
                    d[to[0]][to[1]][v[2]] = d[v[0]][v[1]][v[2]] + 1
                    p[to[0]][to[1]][v[2]] = v
                    q.append([to[0],to[1],v[2]])
            elif v[2] > 0:
                if d[to[0]][to[1]][v[2] - 1] == 1000000:
                    d[to[0]][to[1]][v[2] - 1] = d[v[0]][v[1]][v[2]] + 1
                    p[to[0]][to[1]][v[2] - 1] = v
                    q.append([to[0], to[1], v[2] - 1])

def path(i, j, k):
    pt = []
    while p[i][j][k] != -1:
        pt.append([i,j,k])
        i,j,k = p[i][j][k][0], p[i][j][k][1], p[i][j][k][2]
    return pt[::-1]

def int_1(a):
    return int(a) - 1

def step(i, j):
    ans = []
    if i != 0:
        ans.append([i - 1, j])
    if i != n - 1:
        ans.append([i + 1, j])
    if j != 0:
        ans.append([i, j - 1])
    if j != m - 1:
        ans.append([i, j + 1])
    return ans

n, m, k= map(int, input().split())
x1, y1 = map(int_1, input().split())
x2, y2 = map(int_1, input().split())
g = [[int(i) for i in input().split()]for _ in range(n)]
d = [[[1000000] * (k + 1) for i in range(m)] for _ in range(n)]
p = [[[-1] * (k + 1) for i in range(m)] for _ in range(n)]
bfs(x1, y1, k)
mn = min(d[x2][y2])
if mn == 1000000:
    print('no path')
    exit(0)
print(mn)
for i in range(len(d[x2][y2]) - 1, -1 , -1):
    if d[x2][y2][i] == mn:
        print(*path(x2,y2,i))
        break
for i in range(len(d[x2][y2]) - 1, -1 , -1):
    if d[x2][y2][i] != 1000000:
        print(d[x2][y2][i])
        print(*path(x2,y2,i))
        break

#print(path(x2,y2))
