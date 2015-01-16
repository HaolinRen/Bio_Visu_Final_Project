from tulip import *

#==================================================================================================#
#||  Date   ||   Hour   ||  Stock  || Share || Transcation  || Values || money || kind  ||   Sum  ||
#===================================================================================================
#|| 23/2/11 || 12:32:00 ||   IBM   ||  23   ||   "Sold"     ||  223   ||  USD  || cost  || 232,23 ||
#===================================================================================================
#|| 23/1/13 || 12:32:23 ||   WAG	 ||  23   ||  "Acquired"  ||  23,2  ||  EU   ||income || 332,2  ||
#===================================================================================================
##Matrix := [[[year, month, day],Transcation,Stock,money,Shares,Values,node],...]

EURTODOLLAR = 1.3
HKDTODOLLAR = 0.1289

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
			oneShare.append(self.__exchangeToDollar(moneyKind, value))
			
			oneShare.append(node)
			
			self.__Matrix.append(oneShare)
		self.__Matrix.sort()

	def getMatrix(self):
		return self.__Matrix
		
	def __exchangeToDollar(self, moneyKind, value):
		if moneyKind == "EUR":
			return value * EURTODOLLAR
		elif moneyKind == "HKD":
			return value * HKDTODOLLAR
		else:
			return value 










