from textToP_StockInfo import ExchangeProperties
from MatrixObject import *

#ExchangeProperties = {'ID':['PLACE','SECTOR','INDUSTRY','SubIndustry']}
#propertyMatrix: [[name,[propertyList],[Share],[Value],[Node]]...]

PROP_CITY = 0
PROP_SECTOR = 1
PROP_INDUSTRY = 2
PROP_SUB_INDUSTRY = 3

STOCK_NAME = 0
STOCK_PROP = 1
STOCK_SHARE = 2
STOCK_VALUE = 3
STOCK_NODE = 4
STOCK_LEN = 5

class StockPropertyMatrix(MatrixObject):
	def __init__(self, formerMatrix):
		self.__propertyMatrix = self.getPrpertyMatrix()	

	def getPrpertyMatrix(self, formerMatrix):
		propertyMatrix = []
		for item in formerMatrix:
			if item[TRANSACTION] == 'Acquired':
				oneStockProperty = []
				stockFullName = item[STOCK]
				stockPropertyList = self.getStockPropertyList(stockFullName)
				oneStockProperty.append(stockFullName)
				oneStockProperty.append(stockPropertyList)
				oneStockProperty.append(item[SHARE])
				oneStockProperty.append(item[VALUE])
				oneStockProperty.append(item[NODE])
				propertyMatrix.append(oneStockProperty)
		return propertyMatrix

	def get

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

	def getStockPropertyList(self, stockName):
		res = []
		query = key.split('(')[1].split(')')[0]
		if query == 'HEID':
			query = 'HEI'
		elif query == 'MRKK':
			query = 'MRK'
		elif query == 'FP':
			query = 'FP:FP'
		elif ' ' in query:
			query = query.replace(' ','/')

		for key in stockTimesDict.keys():
			if query in key:
				res = stockTimesDict[key]
				break
		return res

	def getTreeStruture(self, choice = 0):
		treeDict = []
		for key in ExchangeProperties.keys():
			res = ExchangeProperties[key][choice:]
			if res not in treeDict:
				treeDict.append(res)
		return treeDict

