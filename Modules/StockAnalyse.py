from MatrixObject import *

class StockAnalyse(MatrixObject):
	def __init__(self,matrix):
		self.stockCostDict = self.formSotckCostDict(matrix)

	def formSotckCostDict(self, matrix):
		res = {}
		for item in matrix:
			if item[TRANSCATION] == 'Acquired':
				stockName = item[STOCK]
				stockCost = item[SHARE] * item[VALUE]
				if stockName not in res.keys():
					oneStock = [stockCost]
					res[stockName] = oneStock
				else:
					res[stockName].append(stockCost)
		return res
		
	def getStockDict(self):
		return self.stockCostDict
		
	def getStockTimes(self):
		result = {}
		for stockName in self.stockCostDict:
			buyTimes = len(self.stockCostDict[stockName])
			result[stockName] = buyTimes
		return result
		
	def getStockSumCost(self):
		result = {}
		for stockName in self.stockCostDict:
			buyCost = sum(self.stockCostDict[stockName])
			result[stockName] = buyCost
		return result



