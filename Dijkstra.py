def Dijkstra(s):
	INF = 1000000000
	d[s] = 0
	for i in range(n):
		v = -1
		for j in range(n):
			if not u[j] and (v == -1 or d[j] < d[v]):
				v = j
		if d[v] == INF:
			break
		u[v] = True
		for to in g[v]:
			if to[1] >= d[v] and (to[2] < d[to[0]]):
				d[to[0]] = to[2]
				p[to[0]] = v

def path(b):
	pt = []
	while b != -1:
		pt.append(b + 1)
		b = p[b]
	return pt[::-1]


INF = 1000000000
n = int(input())
a, b = map(int, input().split())

g = [[] for i in range(n)]
for _ in range(int(input())):
	a_1,t1,a_2,t2 = map(int, input().split())
	g[a_1 - 1].append([a_2 - 1, t1,t2])

d = [INF] * n
p = [-1] * n
u = [False] * n
Dijkstra(a)
print(d[b - 1] if d[b - 1] != INF else -1)
