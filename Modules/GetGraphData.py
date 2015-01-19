from tulip import *
from ExchangeRate import *

#==================================================================================================#
#||  Date   ||   Hour   ||  Stock  || Share || Transcation  || Values || money || kind  ||   Sum  ||
#===================================================================================================
#|| 23/2/11 || 12:32:00 ||   IBM   ||  23   ||   "Sold"     ||  223   ||  USD  || cost  || 232,23 ||
#===================================================================================================
#|| 23/1/13 || 12:32:23 ||   WAG	 ||  23   ||  "Acquired"  ||  23,2  ||  EU   ||income || 332,2  ||
#===================================================================================================
##Matrix := [[[year, month, day],Transcation,Stock,money,Shares,Values,node],...]


class GetGraphData():
	def __init__(self, graph):
		self.graph = graph
		self.__Matrix = []
		self.Date = self.graph.getStringProperty("Date")
		self.Hour = self.graph.getStringProperty("Hour")
		self.Shares = self.graph.getStringProperty("Shares")
		self.Stock = self.graph.getStringProperty("Stock")
		self.Transaction = self.graph.getStringProperty("Transaction")
		self.Value = self.graph.getStringProperty("Value")
		self.Money = self.graph.getStringProperty("money")
		self.Hour = self.graph.getStringProperty("Hour")
		self.__formeMatrix()

	def __getDateList(self, dateList):
		tempDateList = dateList
		tempDateList.reverse()
		tempDateList = [int(i) for i in tempDateList]
		return tempDateList
		
	def __formeMatrix(self):
		for node in self.graph.getNodes():
			if not self.Stock.getNodeValue(node):
				continue
			oneShare = []
			tiem = self.Date.getNodeValue(node)
			tempDateList = self.Date.getNodeValue(node).split('/')
			tempDateList = self.__getDateList(tempDateList)
			oneShare.append(tempDateList)
			
			hour = self.Hour.getNodeValue(node)[0:5]
			oneShare.append(hour)

			oneShare.append(self.Transaction.getNodeValue(node))
			oneShare.append(self.Stock.getNodeValue(node))
			moneyKind = self.Money.getNodeValue(node)
			if moneyKind == '':
				moneyKind = 'USD'
			oneShare.append(moneyKind)

			oneShare.append(float(self.Shares.getNodeValue(node).replace(',','.')))
			value = float(self.Value.getNodeValue(node).replace(',','.'))
			oneShare.append(self.__exchangeToDollar(moneyKind, value,tempDateList))
			
			oneShare.append(node)
			
			self.__Matrix.append(oneShare)
		self.__Matrix.sort()

	def getMatrix(self):
		return self.__Matrix
		
	def dateListToString(self,dateList):
		date = '20' + str(dateList[0]) + '.' + str(dateList[1]) + '.'
		if dateList[2] < 10:
			day = '0' + str(dateList[2])
		else:
			day = str(dateList[2])
		date += day
		return date			
		
	def __exchangeToDollar(self, moneyKind, value, tempDateList):
		if moneyKind == "HKD":
			exchangeRate = 0.129
		elif moneyKind == "EUR":	
			try:
				date = self.dateListToString(tempDateList)
				rateDict = EUR_USD_Rate_Dict
				exchangeRate = rateDict[date]
			except:
				exchangeRate = 0.3746
				
		else:
			return value 
		return exchangeRate * value










