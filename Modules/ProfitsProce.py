from MatrixObject import *

class ProfitsProce(MatrixObject):

	def __init__(self, matrix):
		self.profitsList = self.preProcess(matrix)
		self.marketProfits = {}

	def netIncome(self):
		res = 0
		for item in self.profitsList:
			res += item
		print "All these years's profits is ", res
		return res	

	def diffMethod(self, soldStock, acquiredStock):
		buyValue = acquiredStock[VALUE]
		soldValue = soldStock[VALUE]
		res = (soldValue - buyValue) * soldStock[SHARE]
		return res

	def diffMarketIncomeYearly(self, matrix):
		marketUS = 0
		marketEU = 0
		marketHK = 0
		index = 0
		for item in matrix:
			if item[TRANSCATION] == 'Acquired':
				if item[MONEY] == 'EUR':
					marketEU += self.profitsList[index]
				elif item[MONEY] == 'HKD':
					marketHK += self.profitsList[index]
				else:
					marketUS += self.profitsList[index]
				index += 1
				if index == len(self.profitsList):
					break
		res = {'USA':marketUS, 'EUROPE':marketEU, 'HK':marketHK}
		return res

	
	# firstDay = matrix[DATE][0]		
	# day1 = datetime(firstDay[0],firstDay[1],firstDay[2])
	
