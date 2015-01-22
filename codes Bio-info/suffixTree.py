
root = []

parttern = 'faofjeoqnfoffaaf'


def simpleSuffixTreeAlgorithm(T):
	root = {}
	for i in range(len(T)):
		node = root
		while True:
			if T[i] not in node.keys():
				node[T[i]] = {}
				break
			else:
				node = node[T[i]]
				print node
	
simpleSuffixTreeAlgorithm("abcdabcd")


