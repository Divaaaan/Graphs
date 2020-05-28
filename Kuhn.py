def try_kuhn (v):
	if used[v]:
		return False
	used[v] = True
	for to in g[v]:
		if mt[to] == -1 or try_kuhn(mt[to]):
			mt[to] = v
			return True
	return False
 
mt = [-1] * k

# for i in range(n):
# 	for x in g[i]:
# 		if mt[x] == -1:
# 			mt[x] = i
# 			break

used = [0] * n
for v in range(n):
	if try_kuhn(v):
		used = [0] * n
 
for i in range(k):
	if mt[i] != -1:
		print(mt[i]+1, i+1)
