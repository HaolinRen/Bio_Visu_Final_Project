from graphObject import *
import calendar

DATE = 0
HOUR = 1
TRANSACTION = 2
STOCK = 3
MONEY = 4
SHARE = 5
VALUE = 6
NODE = 7
LEN = 8

class LayoutInit(graphObject):
	"""docstring for LayoutInit"""
	def __init__(self,graph):
		graphObject.__init__(self, graph)

	def setLayoutInit(self, matrix):
		self.clearNodes()	
		x1 = y1 = 0
		x2 = 200
		y2 = 0
		distX = 1
		distY = 2
		for item in matrix:
			self.setNodeS(item[NODE])
			stockShortName = self.getStockShortForm(item[STOCK])
			if item[MONEY] == 'EUR':
				colorMarket = Color_red
			elif item[MONEY] == 'HKD':
				colorMarket = Color_blue
			else:
				colorMarket = Color_tan
			if item[TRANSACTION] == "Acquired":
				self.setNodeC(item[NODE],x1, y1, colorMarket)
				self.addLabel(item[NODE],stockShortName,Label_left)
			else:
				self.setNodeC(item[NODE],x2, y2, colorMarket)
				self.addLabel(item[NODE],stockShortName,Label_right)
			x1 += distX
			x2 += distX
			y1 += distY
			y2 += distY

	def setLayoutInit2(self, matrix):
		self.clearNodes()
		lastDay = ''
		cordX = 0
		colorTestDict = {}
		hourTestList = []
		daysTestList = []
		for item in matrix:
			if item[STOCK] not in colorTestDict.keys():
				color = self.giveRandomColor()
				colorTestDict[item[STOCK]] = color
			else:
				color = colorTestDict[item[STOCK]]

			if item[TRANSACTION] == 'Sold':
				shapeNode = Shape_circle
			else:
				shapeNode = Shape_cubeOutlined

			today = item[DATE][2]
			todayDetail = '20%i.%i'%(item[DATE][0],item[DATE][1])
			hours = int(item[HOUR][0:2])
			minutes = int(item[HOUR][3:5])
			cordY = hours * cubeSize * 13 + minutes * cubeSize
			if hours not in hourTestList:
				hourTestList.append(hours)
				hoursInfo = item[HOUR][0:5]
				self.addInfo(0, cordY,hoursInfo)
			if todayDetail not in daysTestList:
				daysTestList.append(todayDetail)
				self.addInfo(cordX,0, todayDetail)

			size = item[VALUE] * item[SHARE] / 10
			self.setNodeS(item[NODE],size,size,shapeNode)
			self.setNodeC(item[NODE],cordX,cordY,color)
			if lastDay != today:
				cordX += cubeDistance
				lastDay = today

	def setLayoutDays(self, matrix):
		self.clearNodes()	
		self.clearAllEdges()
		self.clearLabel()
		M = len(matrix)
		lastMonth = matrix[0][0][1]
		x = y = 0
		
				
		def drawCube():
			self.addInfo(400, 50, "ADM's Activity")
			startMonth = lastMonth
			cordX = cordY = 0
			Aindex = 0
			for year in range(2011, 2015):
				for month in range(startMonth, 13):
					monthRange = calendar.monthrange(year, month)[1]
					for days in range(1, monthRange + 1):
						cordX = days * cubeDistance
						
						tempNode = self.graph.addNode()
						self.setNodeC(tempNode, cordX, cordY, Color_yellow, -1)
						self.setNodeS(tempNode, cubeSize, cubeSize, Shape_cube)
						if cordX == cubeDistance and month == startMonth:
							self.addLabel(tempNode, str(year) + '. '+str(month)+'  ', Label_left,Color_red)
						elif cordX == cubeDistance:
							self.addLabel(tempNode, str(month) + '  ', Label_left)

						self.addToAllSubgraph(tempNode)
					cordY -= cubeDistance
					if month == 12:
						startMonth = 1
						cordY -= cubeDistance
		drawCube()
		for itemIndex in range(M):
			item = matrix[itemIndex]
			x = item[0][2] * cubeDistance
			if item[0][1] != lastMonth:
				y -= cubeDistance
				if item[0][1] == 1:
					y -= cubeDistance
				lastMonth = item[0][1]
			self.setNodeS(item[NODE],cubeSize,cubeSize, Shape_cube,2)
#			self.viewLayout[item[NODE]] = tlp.Coord(x, y,2)
			if item[TRANSACTION] == 'Acquired':
				nodeColor = Color_red
			else:
				nodeColor = Color_blue
			self.setNodeC(item[NODE],x,y,nodeColor)
			
	def addEdge(self, matrix):
		tempNode = self.graph.getOneNode()
		if not self.Stock.getNodeValue(tempNode):
			print 'Clear the nodes first!'
			return 0
		if self.graph.deg(tempNode) != 0:
			return 0
		alreadySoldList = []
		M = len(matrix)
		for itemIndex in range(M):
			if matrix[itemIndex][TRANSACTION] == "Acquired":
				tempAcquiredStock = matrix[itemIndex]
				acquiredNum = tempAcquiredStock[SHARE]
				for soldIndex in range(itemIndex + 1, M):
					if matrix[soldIndex][STOCK] == tempAcquiredStock[STOCK]:
						if matrix[soldIndex][TRANSACTION] == "Sold":
							if matrix[soldIndex][SHARE] == acquiredNum:
								if soldIndex not in alreadySoldList:
									self.graph.addEdge(matrix[soldIndex][NODE],tempAcquiredStock[NODE])
									alreadySoldList.append(soldIndex)
									break


	def addSubgraphEveryYear(self):
		if self.graph.getSubGraph("Years"):
			return 0
		subGraphYears = self.graph.addSubGraph("Years")
		subGraph11 = subGraphYears.addSubGraph("2011")
		subGraph12 = subGraphYears.addSubGraph("2012")		
		subGraph13 = subGraphYears.addSubGraph("2013")
		subGraph14 = subGraphYears.addSubGraph("2014")

		for node in self.graph.getNodes():
			if not self.Date.getNodeValue(node):
				continue
			year = self.Date.getNodeValue(node).split('/')[2]
			
			if year == '11':
				subGraph11.addNode(node)
			elif year == '12':
				subGraph12.addNode(node)
			elif year == '13':
				subGraph13.addNode(node)
			else:
				subGraph14.addNode(node)
			
		print 'Added the subgraphs of years.'

	def addSubgraphDifferentMarket(self):
		if self.graph.getSubGraph("Markets"):
			return 0
		subGraphMarkets = self.graph.addSubGraph("Markets")
		subGraphUSA = subGraphMarkets.addSubGraph("US")
		subGraphEUR = subGraphMarkets.addSubGraph("EU")
		subGraphHK = subGraphMarkets.addSubGraph("HK")
		for node in self.graph.getNodes():
			if not self.Stock.getNodeValue(node):
				continue
			money = self.Money.getNodeValue(node)
			if money == 'EUR':
				subGraphEUR.addNode(node)
			elif money == 'HKD':
				subGraphHK.addNode(node)
			else:
				subGraphUSA.addNode(node)
		else:
			print 'Added the subgraph of different markets.'

	def addSubgraphDifferentStocks(self):
		if self.graph.getSubGraph('Stocks'):
			return 0
		subGraphStocks = self.graph.addSubGraph('Stocks')
		
		for node in self.graph.getNodes():
			if not self.Stock.getNodeValue(node):
				continue
			stockName = self.Stock.getNodeValue(node) 
			try:
				stockSubgraph = subGraphStocks.getSubGraph(stockName)
				stockSubgraph.addNode(node)
			except:
				stockSubgraph = subGraphStocks.addSubGraph(stockName)
				stockSubgraph.addNode(node)
		else:
			print 'Added the subgraphs of differents stocks.'

	def addSubgraphTransaction(self):
		if self.graph.getSubGraph('Transaction'):
			return 0
		subGraphTransaction = self.graph.addSubGraph('Transaction')
		subGraphSold = subGraphTransaction.addSubGraph('Sold')
		subGraphAcquired = subGraphTransaction.addSubGraph('Acquired')
		for node in self.graph.getNodes():
			if not self.Transaction.getNodeValue(node):
				continue
			if self.Transaction.getNodeValue(node) == 'Sold':
				subGraphSold.addNode(node)
			else:
				subGraphAcquired.addNode(node)
		else:
			print 'Added the subgraphs based on transaction.'


