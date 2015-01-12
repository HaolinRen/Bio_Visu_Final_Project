fileP = open('/Users/REN/Downloads/textToP_StockInfo.py', 'w')
fileT = open('/Users/REN/Downloads/StockInfoSearchResults.txt', 'r')

fileP.write('ExchangeProperties = {\n')

contents = fileT.readlines()
index = 0
try:
	while index < len(contents):
		stockID = "'%s'"%(contents[index].replace('\n',''))
		fileP.write(stockID + ':')
		property1 = "'%s'"%(contents[index + 1].split(':')[1].replace('\n',''))
		property2 = "'%s'"%(contents[index + 2].split(':')[1].replace('\n',''))
		property3 = "'%s'"%(contents[index + 3].split(':')[1].replace('\n',''))
		property4 = "'%s'"%(contents[index + 4].split(':')[1].replace('\n',''))
		fileP.write('[%s,%s,%s,%s],\n'%(property3,property4,property2,property1))
		index += 5
	else:
		fileP.write('}\n')
except:
	print 'fileWrite Error'
	
fileP.close()
fileT.close()