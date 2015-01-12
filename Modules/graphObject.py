
from tulip import *

Shape_cube = tlp.NodeShape.Cube 
Shape_cubeOutlined = tlp.NodeShape.CubeOutlined
Shape_circle = tlp.NodeShape.Circle

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

	def delSubGraphs(self):
		for subGraph in self.graph.getSubGraphs():
			self.graph.delAllSubGraphs(subGraph)
			
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
				

