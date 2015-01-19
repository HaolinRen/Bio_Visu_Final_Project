from graphObject import *
from ExchangeRate import *
from GetPropertyMatrix import *

DATE = 0
HOUR = 1
TRANSACTION = 2
STOCK = 3
MONEY = 4
SHARE = 5
VALUE = 6
NODE = 7
LEN = 8

class StockAnalyse(graphObject):
	def __init__(self,graph):
		graphObject.__init__(self,graph)
	
	def getMostBuyStock(self, nameDict):
		res = {}
		for key in nameDict.keys():
			if len(nameDict[key][1]) >19:
				res[key] = nameDict[key][1]
		print 'There %i stocks bought more then 10 times.'%(len(res))
		return res
	
	def addSubgraphMostBuy(self, nameDict):	
		
		if self.graph.getSubGraph('MostBuy'):
			return 0
		nodeDict = self.getMostBuyStock(nameDict)
		subGraph = self.graph.addSubGraph('MostBuy')
		for key in nodeDict.keys():
			tempSub = subGraph.addSubGraph(key)
			for node in nodeDict[key]:
				tempSub.addNode(node)
		else:
			print '"MostBuy" subgraph added.' 				
		
	def mostBuylayout(self, matrix):
		if len(matrix) > 50:
			print 'Need operate in most buy subgraph'
			return 0
		self.clearNodes()
		self.makeEspace()
		self.clearAllEdges()
		x = y = 0
		totalHeight = 14
		initialHeight = matrix[0][SHARE]
		nodeList = []
		for item in matrix:
			y = item[VALUE]
			if item[TRANSACTION] == 'Sold':
				color = Color_red
			else:
				color = Color_blue
			nodeList.append(item[NODE])
			height = float(item[SHARE]) /initialHeight * totalHeight
			self.setNodeS(item[NODE],1,height,Shape_cubeOutlined)
			self.setNodeC(item[NODE],x,y,color)
			if color == Color_red:
				x += 3		
			x += 1
		
		for i in range(len(nodeList) - 1):
			self.graph.addEdge(nodeList[i],nodeList[i+1])
		
		
