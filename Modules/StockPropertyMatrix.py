from textToP_StockInfo import ExchangeProperties

#'SAP:GR':['Xetra','Technology','Software','ApplicationSoftware']

CITY = 0
SECTOR = 1
INDUSTRY = 2
SUB_INDUSTRY = 3

class StockPropertyMatrix(object):
	def __init__(self):
		pass	
	
	def stockMarketInfo(self, index):
		stockProperty = []
		for item in ExchangeProperties.keys():
			if ExchangeProperties[item][index] not in stockProperty:
				stockProperty.append(ExchangeProperties[item][index])
		return stockProperty
		
	def stockInfoIntro(self):
		stockProperties = [[],[],[],[]]
		for i in range(4):
			stockProperties[i] = self.stockMarketInfo(i)
		print 'All the stocks all bought from %i stock markets:'%(len(stockProperties[0])-1)
		print stockProperties[0]
		print 'Thoese stocks are in %i sectors:'%(len(stockProperties[1]))
		print stockProperties[1]
		print 'continue'
	
	def getStockPropertyMatrix(self, stockTimesDict):
		propertyMatrix = []
		for key in stockTimesDict.keys():
			query = key.split('(')[1].split(')')[0]
			if query == 'HEID':
				query = 'HEI'
			elif query == 'MRKK':
				query = 'MRK'
			elif query == 'FP':
				query = 'FP:FP'
			elif ' ' in query:
				query = query.replace(' ','/')
				
			for key2 in ExchangeProperties.keys():
				if query in key2:
					tempNewList = [key] + [ExchangeProperties[key2]] + [stockTimesDict[key]]
					propertyMatrix.append(tempNewList)
					break
		return propertyMatrix
			
			
