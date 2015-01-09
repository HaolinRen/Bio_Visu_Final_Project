
file = open('/Users/REN/Documents/StockSearchResults.txt','r')
file2 = open('/Users/REN/Documents/StockInfoSearchResults.txt','w')
contents = file.readlines()

for item in contents:
	res = item.replace(' ','')
	if res == '\n':
		continue
	file2.write(res)

file.close()
file2.close()
