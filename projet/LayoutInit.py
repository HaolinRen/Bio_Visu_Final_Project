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
			self.setNodeS(item[NODE],3,3)
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

	def setLayoutInit(self, matrix):
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

	def setLayoutIncomeInit(self, matrix, dataList):
		x = y = 0
		index = 0
		NumOfCubesInOneLine = 25
		for item in matrix:
			if item[TRANSACTION] == "Acquired":
				if index < len(dataList):
					stockID = self.getStockShortForm(item[STOCK])
					self.addLabel(item[NODE],stockID,Label_center)
					self.setNodeS(item[NODE], cubeSize, cubeSize, Shape_cubeOutlined)
					if dataList[index] > 0:	
						self.setNodeC(item[NODE],x, y, Color_red)
					else:
						self.setNodeC(item[NODE],x, y, Color_green)
					index += 1
					x += cubeDistance
					if x > NumOfCubesInOneLine * cubeDistance:
						x = 0
						y -= cubeDistance
				else:
					self.setNodeC(item[NODE])
					self.setNodeS(item[NODE])

			else:
				self.setNodeC(item[NODE])
				self.setNodeS(item[NODE])

	#full data
	def setLayoutIncomeStick(self, matrix, dataList, choice = 0):
		x = y = 0
		index = 0
		for item in matrix:
			if item[TRANSACTION] == "Acquired":
				if index < len(dataList):
					if choice == 0:
						nodeInfo = str(dataList[index]) + item[STOCK]
						if dataList[index] < -1000:
							sizeStick = -600 * cubeSize
						else:
							sizeStick = dataList[index] * cubeSize
					elif choice == 1:
						nodeInfo = str(round(dataList[index]))
						sizeStick = dataList[index]

					y = sizeStick / 2
					self.setNodeC(item[NODE], x, y, Color_green)
					self.setNodeS(item[NODE], cubeSize, sizeStick, Shape_cubeOutlined)
					self.addLabel(item[NODE], nodeInfo, Label_top)
				else:
					self.setNodeS(item[NODE])
					self.setNodeC(item[NODE])
				index += 1
				x += cubeDistance
			else:
				self.setNodeC(item[NODE])
				self.setNodeS(item[NODE])

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

	
