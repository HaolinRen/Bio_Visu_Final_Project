from tulip import *


#Date       Hour     Stock Share Transcation Values  money  kind     Sum
#23/2/11   12:32:00   IBM   23	   "Sold"     223    USD    cost    232,23
#23/32/13  12:32:23   WAG	  23    "Acquired"  23,2   EUR	income	 332,2
#
#Matrix := [[[year, month, day],Transcation,Stock,money,Shares,Values,node]

class GetGraphData():
	def __init__(self, graph):
		self.graph = graph
		self.__Matrix = []
		self.Date = self.graph.getStringProperty("Date")
		self.Shares = self.graph.getStringProperty("Shares")
		self.Stock = self.graph.getStringProperty("Stock")
		self.Transaction = self.graph.getStringProperty("Transaction")
		self.Value = self.graph.getStringProperty("Value")
		self.Money = self.graph.getStringProperty("money")
		self.__formeMatrix()

	def __getDateList(self, dateList):
		tempDateList = dateList
		tempDateList.reverse()
		tempDateList = [int(i) for i in tempDateList]
		return tempDateList
		
	def __formeMatrix(self):
		for n in self.graph.getNodes():
			if not self.Stock.getNodeValue(n):
				break
			oneShare = []
			tempDateList = self.Date.getNodeValue(n).split('/')
			tempDateList = self.__getDateList(tempDateList)
			oneShare.append(tempDateList)
			oneShare.append(self.Transaction.getNodeValue(n))
			oneShare.append(self.Stock.getNodeValue(n))
			oneShare.append(self.Money.getNodeValue(n))
			oneShare.append(float(self.Shares.getNodeValue(n).replace(',','.')))
			oneShare.append(float(self.Value.getNodeValue(n).replace(',','.')))			
			oneShare.append(n)
			self.__Matrix.append(oneShare)
		self.__Matrix.sort()

	def getMatrix(self):
		return self.__Matrix

	

