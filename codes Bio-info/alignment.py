str1 = "ATG";
str2 = "AAGC";

para1 = 2
para2 = 2
para3 = 1

def getMet(str1, str2):
	dist = []
	for k in range(len(str1) + 1):
		temp = []
		for j in range(len(str2) + 1):
			temp.append(0)
		dist.append(temp)
	for i in range(len(dist[0])):
		for k in range(len(dist)):
			if i == 0 and k == 0:
				continue
			else:
				if i == 0:
					dist[k][i] = dist[k - 1][i] - para1
				elif k == 0:
					dist[k][i] = dist[k][i - 1] - para1
				else:
					if str1[k-1] == str2[i-1]:
						index = para3
					else:
						index = -para3
					dist[k][i] = max(dist[k-1][i]-para1, dist[k][i-1]-para1,dist[k-1][i-1]+index)


	return dist


res = getMet(str1, str2)
for i in range(len(res[0])):
	for j in range(len(res)):
		print res[j][i],
	print



