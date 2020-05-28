def prefix_function (s):
	n = len(s)
	pi = [0] * n
	for i in range(1, n):
		j = pi[i - 1]
		while j > 0 and s[i] != s[j]:
			j = pi[j-1]
		if s[i] == s[j]:
			j += 1
		pi[i] = j
	return pi

s = input()
s1 = '>>-->#' + s
s2 = '<--<<#' + s
p1 = prefix_function(s1)
p2 = prefix_function(s2)
k = 0
for i in range(len(p1)):
	if p1[i] == 5:
		k += 1
	if p2[i] == 5:
		k += 1
print(k)
