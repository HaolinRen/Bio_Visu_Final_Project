
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

	def giveRandomColorList(self):
		c1 = random.randint(0,255)
		c2 = random.randint(0,255)
		c3 = random.randint(0,255)
		return [c1,c2,c3]

	def giveTheColorOfList(self, colorList):
		c1 = colorList[0]
		c2 = colorList[1]
		c3 = colorList[2]
		colorOfList = tlp.Color(c1,c2,c3)
		return colorOfList

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
	
	def addInfo(self, x, y, info, position = Label_bottom):
		tempNode = self.graph.addNode()
		self.setNodeC(tempNode, x, y)
		self.setNodeS(tempNode)
		self.addLabel(tempNode, info, position)
		self.addToAllSubgraph(tempNode)
		
	def getStockShortForm(self, stockName):
		try:
			return stockName.split('(')[1].split(')')[0]
		except:
			return stockName
	
	def delSubGraphs(self):
		for subGraph in self.graph.getSubGraphs():
			self.graph.delAllSubGraphs(subGraph)
		else:
			print 'subgraphs deleted.'

	def deleteSubgraphsOfStocks(self):
		subgraphStock = self.graph.getSubGraphs('Stock')
		self.graph.delAllSubGraphs(subgraphStock)
		print 'subgraphs of stocks are deleted.'

	def addToAllSubgraph(self, node):
		try:
			subgraphs = self.graph.getSubGraphs()
			for subgraph in subgraphs:
				subs = subgraph.getSubGraphs()
				for sub in subs:
					sub.addNode(node)
		except:
			print 'You need add subgraphs first!'	
	
	def addStickGraph(self, dic,fullsize,startX = 0, startY =0):
		self.clearNodes()
		stickX = startX
		stickY = startY
		fullWidth = fullsize
		sumsOfDic = 0
		for key in dic.keys():
			sumsOfDic += dic[key]
		height = fullWidth / len(dic.keys())
		for key in dic.keys():
			tempNode = self.graph.addNode()
			percent = float(dic[key]) / sumsOfDic
			width = percent * fullWidth
			stickX = width / 2
			color = self.giveRandomColor()
			self.setNodeC(tempNode, stickX, stickY, color)
			self.setNodeS(tempNode, width, height, Shape_cubeOutlined)
			labelInfo = str(percent*100)[0:4] + '%'
			self.addLabel(tempNode,labelInfo, Label_center)
			self.addInfo(-10,stickY,key,Label_left)
			stickY -= height


