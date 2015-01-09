from MatrixObject import *
from stockKinds import *

STOCK_COST = 0
STOCK_MONEY = 1
STOCK_TIMES = 2

class StockAnalyse(MatrixObject):

	def __init__(self, matrix):
		self.__stockMatrix = self.formSotckMatrix(matrix)

	def formSotckMatrix(self, matrix):
		res = {}
		for item in matrix:
			if item[TRANSCATION] == 'Acquired':
				stockName = item[STOCK]#.split('(')[1].split(')')[0]
				stockCost = item[SHARE] * item[VALUE]
				if stockName not in res.keys():
					oneStock = [stockCost, item[MONEY],1]
					res[stockName] = oneStock
				else:
					res[stockName][STOCK_TIMES] += 1
					res[stockName][STOCK_COST] += stockCost
		return res

	def getStockMatrix(self):
		return self.__stockMatrix
		
	def getMarketsStockNum(self):
		dicNum = {}
		STOCKMARKET_SUM = 0
		STOCKMARKET_TIMES = 1
		marketUS = [0,0]
		marketEU = [0,0]
		marketHK = [0,0]
		
		for key in self.__stockMatrix.keys():
			if self.__stockMatrix[key][STOCK_MONEY] == 'EUR':
				marketEU[STOCKMARKET_SUM] += self.__stockMatrix[key][STOCK_COST]
				marketEU[STOCKMARKET_TIMES] += 1#self.__stockMatrix[key][STOCK_TIMES]
			elif self.__stockMatrix[key][STOCK_MONEY] == 'HKD':
				marketHK[STOCKMARKET_SUM] += self.__stockMatrix[key][STOCK_COST]
				marketHK[STOCKMARKET_TIMES] += 1#self.__stockMatrix[key][STOCK_TIMES]
			else:
				marketUS[STOCKMARKET_SUM] += self.__stockMatrix[key][STOCK_COST]
				marketUS[STOCKMARKET_TIMES] += 1#self.__stockMatrix[key][STOCK_TIMES]
				
		dicNum['USA'] = marketUS
		dicNum['EU'] = marketEU
		dicNum['HK'] = marketHK
		return dicNum
		
	def stockKinds(self):
		sum = 0
#		for i in range(len(StocksTop100USA)):
#			for item in StocksTop100USA[i]:
#				print item, ', '
#				if item in self.__stockMatrix.keys():
#					sum += 1
		for item in self.__stockMatrix.keys():
			print item, ', ',self.__stockMatrix[item]
		
		print sum
