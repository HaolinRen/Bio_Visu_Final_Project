from MatrixObject import *

class StockAnalyse(StockPropertyMatrix):
	def __init__(self,matrix):
		StockPropertyMatrix(self, matrix)
		self.__stockTimes = self.getStockTimes()
		
	def getStockDict(self):
		return self.__stockCostDict

	def getMarketTimes(self):
		return self.__getTimes()

	def getSectorTimes(slef):
		return self.__getTimes(2)
	#get a dict of item and times
	#initial choice is market
	#dict = {'NewYork':23,...}
	def __getTimes(self,choice = 1):
		result = {}
		for key in self.__stockTimes.keys():
			stockPropertyList = self.__stockTimes[key]
			select = stockPropertyList[choice]
			if select not in result:
				result[select] = stockPropertyList[0]
			else:
				result[select] += stockPropertyList[0]
		return result


	# get a dict of sotck times and properties
	#dict = {stockName: [times,market,sector]}
	def getStockTimes(self):
		result = {}
		for stock in self.__propertyMatrix:
			if stock[0] not in result:
				stockPList = [1,stock[1][0],stock[1][2]]
				result[stock] = stockPList
			else:
				result[stock][0] += 1
		return result




