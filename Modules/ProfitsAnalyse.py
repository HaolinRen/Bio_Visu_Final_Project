from MatrixObject import *
STARTMONEY = 11278

class ProfitsAnalyse(MatrixObject):

	def __init__(self, matrix):
		self.__profitsList = self.preProcess(matrix)

	def getProfitsList(self):
		return self.__profitsList

	def netIncome(self, choice = 0):
		res = 0
		earn = lost = 0
		for item in self.__profitsList:
			res += item
			if item > 0:
				earn += 1
			else:
				lost += 1
		print ' '
		if choice == 0:
			print "All these years's profits is %i $"%(res)
		else:
			print 'Earn money %i times'%(earn)
			print 'Lost money %i times'%(lost)
			print 'Forecast accuracy is %s'%str((float(earn)/(earn+lost)*100))[:5], '%.'
		return res	
		
	def liquidSumList(self):
		liquidSum = []
		liquid = STARTMONEY
		for item in self.__profitsList:
			liquid += item
			liquidSum.append(liquid)
		print 'Compared with the original, lost %i $.'%(STARTMONEY - liquidSum[-1])
		return liquidSum

	def diffMethod(self, soldStock, acquiredStock):
		buyValue = acquiredStock[VALUE]
		soldValue = soldStock[VALUE]
		res = (soldValue - buyValue) * soldStock[SHARE]
		return res

	def diffMarketIncomeYearly(self, matrix):
		MARKETPROFITS = 0
		BUYTIMES = 1
		marketUS = [0,0]
		marketEU = [0,0]
		marketHK = [0,0]
		index = 0
		for item in matrix:
			if item[TRANSACTION] == 'Acquired':
				if item[MONEY] == 'EUR':
					marketEU[MARKETPROFITS] += self.__profitsList[index]
					marketEU[BUYTIMES] += 1
				elif item[MONEY] == 'HKD':
					marketHK[MARKETPROFITS] += self.__profitsList[index]
					marketHK[BUYTIMES] += 1
				else:
					marketUS[MARKETPROFITS] += self.__profitsList[index]
					marketUS[BUYTIMES] += 1
				index += 1
				if index == len(self.__profitsList):
					break
		print 'In USA markets %i times transaction are made.'%(marketUS[BUYTIMES])
		print 'USA markets profits %i $'%(marketUS[MARKETPROFITS])
		print 'In EUROPE markets %i times transaction are made.'%(marketEU[BUYTIMES])
		print 'EUROPE markets profits %i $'%(marketEU[MARKETPROFITS])
		print 'In HK markets %i times transaction are made.'%(marketHK[BUYTIMES])		
		print 'HK markets profits %i $'%(marketHK[MARKETPROFITS])
		res = {'USA':marketUS[BUYTIMES], 'EUROPE':marketEU[BUYTIMES], 'HK':marketHK[BUYTIMES]}
		return res

	def buyStockRatePercent(self, matrix):
		result = []
		liquidSum = STARTMONEY
		stockValue = 0
		day = ''
		for item in matrix:
			today = '20%i.%i.%i'%(item[0][0],item[0][1],item[0][2])
			costOrIncome = item[VALUE] * item[SHARE]
			if day == today:
				if item[TRANSACTION] == 'Sold':
					liquidSum += costOrIncome
				else:
					liquidSum -= costOrIncome
					stockValue += costOrIncome
			else:
				if stockValue != 0:
					costPercent = float(stockValue) / (liquidSum + stockValue) * 100
					liquidPercent = (liquidSum + stockValue) / STARTMONEY * 100
					result.append([day,round(costPercent), round(liquidPercent)])
					stockValue = 0
				day = today
				if item[TRANSACTION] == 'Sold':
					liquidSum += costOrIncome
				else:
					liquidSum -= costOrIncome
					stockValue += costOrIncome
		return result
