from fileRead import *


def search(pattern, txt):
	N = len(txt)
	M = len(pattern)
	res = []
	
    for j in range(N-M+1):
        if pattern[0] == txt[j]:
            for k in range(1,M-1):
                if pattern[k] != txt[j+k]:
                    break
            else:
                res.append(j)
    return res

for i in range(len(src)):
	temp = search(pattern1,src[i])
	if temp != []:
		print(i,":",temp)