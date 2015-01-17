from GetGraphData import *
from ShellAlgorithm import ShellAlgorithm
from textToP_StockInfo import ExchangeProperties

#ExchangeProperties = {'ID':['PLACE','SECTOR','INDUSTRY','SubIndustry']}
#propertyMatrix: {name:[[propertyList],[NodeList]]...}
#Tree: [[[propertyList],{name:[node...],name:[...]}]...]

PROP_CITY = 0
PROP_SECTOR = 1
PROP_INDUSTRY = 2
PROP_SUB_INDUSTRY = 3

PROPLIST = 0
NODELIST = 1

class GetPropertyMatrix(GetGraphData):
	def __init__(self, graph):
		self.__sectorsDict = {}
		self.__marketDict = {}
		GetGraphData.__init__(self, graph)
		self.__propertyDict = self.getNameNodeDict()
		self.myShell = ShellAlgorithm()
		
	#[stockID,[propertyList],[node..]]
	def getNameNodeDict(self):
		nameNodeDict = {}
		sectorCount = {}
		marketCount = {}
		for node in self.graph.getNodes():
			if not self.Stock.getNodeValue(node):
				continue
			name = self.Stock.getNodeValue(node)
			proList = self.getStockPropertyList(name)
			stockID = proList[0]
			if proList[2] not in sectorCount:
				sectorCount[proList[2]] = 1
			else:
				sectorCount[proList[2]] += 1
			if proList[1] not in marketCount:
				marketCount[proList[1]] = 1
			else:
				marketCount[proList[1]] += 1
			if stockID not in nameNodeDict:
				nameNodeDict[stockID] = [proList[1:],[node]]
			else:
				nameNodeDict[stockID][NODELIST].append(node)
		self.__sectorsDict = sectorCount
		self.__marketDict = marketCount
#		print self.__sectorsDict
#		print self.__marketDict
		return nameNodeDict

	#{name:[propertyList, cord, size]}
	#return [[id,[property list],node,[cord]]...]
	def getShellMatrix(self):
		result = []
		forShellList = []
		for key in self.__propertyDict.keys():
			propertyList = self.__propertyDict[key]
			tempList = [key, propertyList[PROPLIST][1],propertyList[NODELIST][0]]
			times = len(propertyList[NODELIST])
			forShellList.append(times)
			result.append(tempList)
		myShellList = self.myShell.getShellCord(forShellList)
		for index in range(len(result)):
			result[index].append(myShellList[index])
		print 'ADM8 totally buy %i stocks in thoese 4 years.'%(len(result))
		return result

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
		for i in range(10):
			print i+1,' ',stockProperties[1][i], ', ',
			if i == 5:
				print ''

	def getStockPropertyList(self, stockName):
		res = []
		query = stockName.split('(')[1].split(')')[0]
		if query == 'HEID':
			query = 'HEI'
		elif query == 'MRKK':
			query = 'MRK'
		elif query == 'FP':
			query = 'FP:FP'
		elif ' ' in query:
			query = query.replace(' ','/')
		elif query == 'MT':
			query = 'MT:NA'
		for key in ExchangeProperties.keys():
			if query in key:
				res = [key] + ExchangeProperties[key]
		return res
