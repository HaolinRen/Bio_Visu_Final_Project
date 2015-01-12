from graphObject import *
import calendar

DATE = 0
HOUR = 1
TRANSCATION = 2
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
			if item[TRANSCATION] == "Acquired":
				self.setNodeC(item[NODE],x1, y1, colorMarket)
				self.addLabel(item[NODE],stockShortName,Label_left)
			else:
				self.setNodeC(item[NODE],x2, y2, colorMarket)
				self.addLabel(item[NODE],stockShortName,Label_right)
			x1 += distX
			x2 += distX
			y1 += distY
			y2 += distY

	def setLayoutIncomeInit(self, matrix, dataList):
		x = y = 0
		index = 0
		NumOfCubesInOneLine = 25
		for item in matrix:
			if item[TRANSCATION] == "Acquired":
				if index < len(dataList):
					self.setNodeS(item[NODE], cubeSize, cubeSize, Shape_cubeOutlined)
					if dataList[index] > 0:	
						self.setNodeC(item[NODE],x, y, Color_red)
					else:
						self.setNodeC(item[NODE],x, y, Color_green)
					index += 1
				else:
					self.setNodeC(item[NODE])
					self.setNodeS(item[NODE])
				x += cubeDistance
				if x > NumOfCubesInOneLine * cubeDistance:
					x = 0
					y -= cubeDistance
			else:
				self.setNodeC(item[NODE])
				self.setNodeS(item[NODE])

	def setLayoutIncomeStick(self, matrix, dataList, choice = 0):
		x = y = 0
		index = 0
	
		for item in matrix:
			if item[TRANSCATION] == "Acquired":
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

	def setLayoutDays(self, matrix):

		self.clearNodes()	
		self.clearAllEdges()
		M = len(matrix)
		lastMonth = matrix[0][0][1]
		x = y = 0
		
		def drawCube():
			self.addInfo(400, 50, "ADM's Activity")
			startMonth = lastMonth
			cordX = cordY = 0
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
			if item[TRANSCATION] == 'Acquired':
				nodeColor = Color_red
			else:
				nodeColor = Color_blue
			self.setNodeC(item[NODE],x,y,nodeColor)

	def addStickGraph(self, dic, x):
		stickX = x
		sumsOfHeight = 10 * cubeSize
		sumsOfDic = 0
		for key in dic.keys():
			sumsOfDic += dic[key]
		#add meta node
		for key in dic.keys():
			tempNode = self.graph.addNode()
			percent = dic[key] / sumsOfDic * 100 
			hight = percent * sumsOfHeight
			stickY = hight / 2
			self.setNodeC(tempNode, stickX, stickY)
			self.setNodeS(tempNode, cubeSize, hight, Shape_cubeOutlined)
			labelInfo = str(percent)[0:4] + '%'
			self.addLabel(tempNode,labelInfo, Label_center)
			idNode = self.graph.addNode()
			self.setNodeC(idNode, stickX, 0)
			self.setNodeS(idNode)
			self.addLabel(idNode, key, Label_bottom)
			stickX += cubeDistance
			
	def addEdge(self, matrix):
		tempNode = self.graph.getOneNode()
		if self.graph.deg(tempNode) != 0:
			return 0
		alreadySoldList = []
		M = len(matrix)
		for itemIndex in range(M):
			if matrix[itemIndex][TRANSCATION] == "Acquired":
				tempAcquiredStock = matrix[itemIndex]
				acquiredNum = tempAcquiredStock[SHARE]
				for soldIndex in range(itemIndex + 1, M):
					if matrix[soldIndex][STOCK] == tempAcquiredStock[STOCK]:
						if matrix[soldIndex][TRANSCATION] == "Sold":
							if matrix[soldIndex][SHARE] == acquiredNum:
								if soldIndex not in alreadySoldList:
									self.graph.addEdge(matrix[soldIndex][NODE],tempAcquiredStock[NODE])
									alreadySoldList.append(soldIndex)
									break
