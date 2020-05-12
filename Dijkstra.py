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
			if (d[v] + to[1] < d[to[0]]):
				d[to[0]] = d[v] + to[1]
				p[to[0]] = v
