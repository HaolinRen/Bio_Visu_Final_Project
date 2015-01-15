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
		lastDay = ''
		cordX = 0
		for item in matrix:
			if item[MONEY] == 'HKD':
				color = Color_red
			elif item[MONEY] == 'EUR':
				color = Color_green
			else:
				color = Color_tan

			if item[TRANSACTION] == 'Sold':
				shapeNode = Shape_triangle
			else:
				shapeNode = Shape_circle 

			today = matrix[DATE][2]
			hour = int(matrix[HOUR][0:2])
			cordY = hour * cubeSize
			self.setNodeS(item[NODE],cordX,cordY,color)
			self.setNodeC(item[NODE],1,1,shapeNode)
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

						subgraphs = self.graph.getSubGraphs()
						for subgraph in subgraphs:
							sub = subgraph.getSubGraphs()
							for isub in sub:
								isub.addNode(tempNode)

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
