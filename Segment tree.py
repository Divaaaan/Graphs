def build (v, tl, tr):
	if tl == tr:
		t[v] = a[tl]
	else:
		tm = (tl + tr) // 2
		build(v*2, tl, tm)
		build(v*2+1, tm+1, tr)
		t[v] = t[v*2] + t[v*2+1]

def update(v, tl, tr, pos, new_val):
	if tl == tr:
		t[v] = new_val
	else:
		tm = (tl + tr) // 2
		if pos <= tm:
			update (v*2, tl, tm, pos, new_val);
		else:
			update (v*2+1, tm+1, tr, pos, new_val)
		t[v] = t[v*2] + t[v*2+1]

def summ (v, tl, tr, l, r):
	if l > r:
		return 0
	if l == tl and r == tr:
		return t[v]
	tm = (tl + tr) // 2
	return summ (v*2, tl, tm, l, min(r,tm)) \
		+ summ (v*2+1, tm+1, tr, max(l,tm+1), r)

n = int(input())
a = list(map(int, input().split()))
t = [0] * (4 * n)
build(1, 0, n - 1)
k = int(input())
for i in range(k):
	l, r = map(int, input().split())
	print(summ(1, 0, n - 1, l - 1, r - 1))
