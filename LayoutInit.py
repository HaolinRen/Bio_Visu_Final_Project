from tulip import *
from datetime import datetime
import calendar
import math


class LayoutInit():
	"""docstring for LayoutInit"""
	def __init__(self, graph):
		self.graph = graph
		self.viewColor = self.graph.getColorProperty("viewColor")
		self.viewLayout = self.graph.getLayoutProperty("viewLayout")
		self.viewSize = self.graph.getSizeProperty("viewSize")
		self.viewShape = self.graph.getIntegerProperty("viewShape")		
		
	def addSubgraphEveryYear(self):
		if self.graph.getSubGraph("2014"):
			return 0
		subGraph11 = self.graph.addSubGraph("2011")
		subGraph12 = self.graph.addSubGraph("2012")		
		subGraph13 = self.graph.addSubGraph("2013")
		subGraph14 = self.graph.addSubGraph("2014")

		Date = self.graph.getStringProperty("Date")
		for item in self.graph.getNodes():
			year = Date.getNodeValue(item)
			if "2011" in year:
				subGraph11.addNode(item)
			elif "2012" in year:
				subGraph12.addNode(item)
			elif "2013" in year:
				subGraph13.addNode(item)
			else:
				subGraph14.addNode(item)
				
	def delSubgraphs(self):
		for subGraph in self.graph.getSubGraphs():
			self.graph.delSubGraph(subGraph)

	def clearAllEdges(self):
		self.graph.delEdges(self.graph.getEdges())

	def addEdges(self, matrix):
		tempNode = self.graph.getOneNode()
		if self.graph.deg(tempNode) != 0:
			return 0
		M = len(matrix)
		for itemIndex in range(M):
			if matrix[itemIndex][1] == "Acquired":
				tempAcquiredStock = matrix[itemIndex]
				acquiredNum = tempAcquiredStock[4]
				for soldIndex in range(itemIndex + 1, M):
					if matrix[soldIndex][2] == tempAcquiredStock[2]:
						if matrix[soldIndex][1] == "Sold":
							tempSoldStock = matrix[soldIndex]
							self.graph.addEdge(tempSoldStock[6],tempAcquiredStock[6])
							acquiredNum -= tempSoldStock[4]
							if acquiredNum <= 0:
								break

	def setLayoutInit(self, matrix):
		self.addEdges(matrix)
		x1 = 0
		x2 = 400
		y1 = 1
		y2 = 1
		disX = 2
		disY = 4

		def setNode(x, y, color):
			self.viewLayout[item[6]] = tlp.Coord(x, y)
			self.viewColor[item[6]] = color

		for item in matrix:
			self.viewSize[item[6]] = tlp.Size(1,1,1)
			if item[1] == "Acquired":
				color = tlp.Color.Red
				setNode(x1, y1, color)
			else:
				color = tlp.Color.Blue
				setNode(x2, y2, color)
				
			x1 += disX
			x2 += disX
			y1 += disY
			y2 += disY


	def setLayoutInit2(self, matrix):
		self.clearAllEdges()
		self.clearNodes()	
		M = len(matrix)
		cubeSize = 20	
		cubeDistance = cubeSize + cubeSize/3
		firstDay = matrix[0][0]		
		day1 = datetime(firstDay[0],firstDay[1],firstDay[2])
	
		def addCube(x, y):
			tempNode = self.graph.addNode()
			self.viewColor[tempNode] = tlp.Color.Yellow
			self.viewShape[tempNode] = tlp.NodeShape.Cube
			self.viewSize[tempNode] = tlp.Size(cubeSize, cubeSize,0)
			self.viewLayout[tempNode] = tlp.Coord(x, y)
			
		def drawCube():
			startMonth = day1.month
			cordY = cubeDistance
			for year in range(2011, 2015):
				for month in range(startMonth, 13):
					monthRange = calendar.monthrange(year, startMonth)[1]
					for days in range(1, monthRange + 1):
						addCube(days * cubeDistance, cordY)
					startMonth += 1
					cordY -= cubeDistance
					if startMonth == 13:
						startMonth = 1
		drawCube()

		x = y = cubeDistance
		lastMonth = matrix[0][0][1]
		for itemIndex in range(M):
			item = matrix[itemIndex]
			x = item[0][2] * cubeDistance
			if item[0][1] != lastMonth:
				y -= cubeDistance
				lastMonth = item[0][1]

			self.viewShape[item[6]] = tlp.NodeShape.Cube
			self.viewSize[item[6]] = tlp.Size(cubeSize,cubeSize,1)
			self.viewLayout[item[6]] = tlp.Coord(x, y)
		

	def clearNodes(self):
		Stock = self.graph.getStringProperty("Stock")
		for node in self.graph.getNodes():
			if Stock.getNodeValue(node):
				continue
			else:
				self.graph.delNode(node)
	
	



