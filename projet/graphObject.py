
from tulip import *
import random

Shape_cube = tlp.NodeShape.Cube 
Shape_cubeOutlined = tlp.NodeShape.CubeOutlined
Shape_circle = tlp.NodeShape.Circle
Shape_triangle = tlp.NodeShape.Triangle

Color_red = tlp.Color.Red
Color_black = tlp.Color.Black
Color_yellow = tlp.Color.Yellow
Color_green = tlp.Color.Green
Color_blue = tlp.Color.Blue
Color_tan = tlp.Color.Tan 
Color_bud = tlp.Color.SpringBud
Color_azure = tlp.Color.Azure

Label_center = tlp.LabelPosition.Center
Label_top = tlp.LabelPosition.Top
Label_bottom = tlp.LabelPosition.Bottom
Label_left = tlp.LabelPosition.Left
Label_right = tlp.LabelPosition.Right

cubeSize = 20	
cubeDistance = cubeSize + cubeSize/3

class graphObject(object):
	def __init__(self, graph):
		self.graph = graph
		self.viewColor = self.graph.getColorProperty("viewColor")
		self.viewLayout = self.graph.getLayoutProperty("viewLayout")
		self.viewSize = self.graph.getSizeProperty("viewSize")
		self.viewShape = self.graph.getIntegerProperty("viewShape")
		self.Money = self.graph.getStringProperty("money")
		self.Date = self.graph.getStringProperty("Date")
		self.Stock = self.graph.getStringProperty("Stock")
		self.Transaction = self.graph.getStringProperty("Transaction")
		self.viewLabel = self.graph.getStringProperty("viewLabel")
		self.viewLabelPosition = self.graph.getIntegerProperty("viewLabelPosition")
		self.viewLabelColor = self.graph.getColorProperty("viewLabelColor")
		self.viewLabelBorderColor =  self.graph.getColorProperty("viewLabelBorderColor")
		self.viewLabelBorderWidth =  self.graph.getDoubleProperty("viewLabelBorderWidth")

	def clearAllEdges(self):
		self.graph.delEdges(self.graph.getEdges())

	def clearNodes(self):
		for node in self.graph.getNodes():
			if self.Stock.getNodeValue(node):
				continue
			else:
				self.graph.delNode(node)
	
	def clearLabel(self):
		for node in self.graph.getNodes():
			self.viewLabel[node] =  ''
			
	def makeEspace(self):
		for node in self.graph.getNodes():
			self.setNodeS(node)
			self.setNodeC(node)

	def giveRandomColor(self):
		c1 = random.randint(0,255)
		c2 = random.randint(0,255)
		c3 = random.randint(0,255)
		rColor = tlp.Color(c1,c2,c3)
		return rColor

	def giveSimColor(self,originColor):
		c1 = originColor[0] + random.randint(-5,5)
		c2 = originColor[0] + random.randint(-5,5)
		c3 = originColor[0] + random.randint(-5,5)
		return [c1, c2, c3]

	def setNodeC(self, node, x=1, y=1, color=Color_yellow,z = 1):
		self.viewLayout[node] = tlp.Coord(x, y, 1)
		self.viewColor[node] = color

	def setNodeS(self, node, SizeX = 1, SizeY = 1, shape = Shape_circle, SizeZ = 1):
		self.viewShape[node] = shape
		self.viewSize[node] = tlp.Size(SizeX, SizeY, SizeZ)
		
	def addLabel(self, node, name, position = Label_bottom, color = Color_black, width = 0):
		self.viewLabelPosition[node] = position		
		self.viewLabel[node] = name
		self.viewLabelColor[node] = color
		self.viewLabelBorderWidth[node] = width
	
	def addInfo(self, x, y, info):
		tempNode = self.graph.addNode()
		self.setNodeC(tempNode, x, y)
		self.setNodeS(tempNode)
		self.addLabel(tempNode, info)
		self.addToAllSubgraph(tempNode)
		
	def getStockShortForm(self, stockName):
		try:
			return stockName.split('(')[1].split(')')[0]
		except:
			return stockName
		
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
			
		print ''
		print 'Subgraphs of years are added.'
	
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

	def delSubGraphs(self):
		for subGraph in self.graph.getSubGraphs():
			self.graph.delAllSubGraphs(subGraph)
					
	def addToAllSubgraph(self, node):
		try:
			subgraphs = self.graph.getSubGraphs()
			for subgraph in subgraphs:
				subs = subgraph.getSubGraphs()
				for sub in subs:
					sub.addNode(node)
		except:
			print 'You need add subgraphs first!'
			
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
			
	def addStickGraph(self, dic):
		self.makeEspace()
		self.clearNodes()
		stickX = 0
		sumsOfHeight = 100 * cubeSize
		sumsOfDic = 0
		for key in dic.keys():
			sumsOfDic += dic[key]
		width = sumsOfHeight / (len(dic.keys())*2)
		#add meta node
		for key in dic.keys():
			tempNode = self.graph.addNode()
			percent = float(dic[key]) / sumsOfDic
			hight = percent * sumsOfHeight
			stickY = hight / 2
			color = self.giveRandomColor()
			self.setNodeC(tempNode, stickX, stickY, color)
			self.setNodeS(tempNode, width, hight, Shape_cubeOutlined)
			labelInfo = str(percent*100)[0:4] + '%'
			self.addLabel(tempNode,labelInfo, Label_center)
			self.addInfo(stickX,0,key)
			stickX += width

