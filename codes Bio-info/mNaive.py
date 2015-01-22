from fileRead import *

def Naive(pattern, txt):
	M = len(pattern)
	N = len(txt)
	res = []
	for i in range(N-M+1):
		if pattern[0] == txt[i]:
			for j in range(1, M):
				if pattern[j] != txt[i+j]:
					break
			else:
				res.append(i)
	return res

for i in range(len(src)):
	temp = Naive(pattern1,src[i])
	if temp != []:
		print "find the same pattern in ", i ,"th: starts at" ,temp