from fileRead import *

def KMP_prefix(pattern):
    M = len(pattern)
    pla = [0]
    k = 0
    for i in range(2,M):
        while k > 0 and pattern[k+1] != pattern[i]:
            k = pla[k]
            if pattern[k+1] == pattern[i]:
                k = k + 1
                pla.append(k)
    return pla

print(KMP_prefix(pattern2))
            

