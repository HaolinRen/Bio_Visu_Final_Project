from fileRead import *

d = 256

def search(pattern, txt, q):
    M = len(pattern)
    N = len(txt)
    p = 0
    t = 0
    h = 1
    res = []
    
    for i in range(M-1):
        h = (h*d)%q
    for j in range(M):
        p = (d * p + ord(pattern[j])) % q
        t = (d * t + ord(txt[j])) % q

    for k in range(N-M+1):
   		if p == t:
   			for temp in range(M):
   				if pattern[temp] != txt[k+temp]:
   					break
   			else:
   				res.append(k)
   		if k < N-M:
   			t = (d*(t - h*ord(txt[k])) + ord(txt[k+M]))%q
   			if t < 0:
   				t = t + q
    return res

for index in range(len(src)):
    temp = search(pattern2,src[index],101)
    if temp != []:
        print("line:",index,":",temp)
