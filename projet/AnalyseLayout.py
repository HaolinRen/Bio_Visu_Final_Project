from graphObject import *

PERCENT_DATE = 0
PERCENT_COST = 1
PERCETN_PROPER = 2

class AnalyseLayout(graphObject):
	def __init__(self,graph):
		graphObject.__init__(self, graph)
		
	def costPencentLayout(self, costRateMatrix):
		self.makeEspace()
		self.clearNodes()
		totalHeight = 100 * cubeSize
		x = y = 0
		for item in costRateMatrix:
			properHeight = totalHeight * item[PERCETN_PROPER]
			costPercent = item[PERCENT_COST]
			costHeight = properHeight * item[PERCENT_COST]
			liquidHeight = properHeight - costHeight
			costNode = self.graph.addNode()
			liquideNode = self.graph.addNode()
			self.setNodeC(liquideNode, x, y + liquidHeight/2, Color_green)
			self.setNodeS(liquideNode, cubeSize, liquidHeight, Shape_cube)
			self.addLabel(liquideNode, item[PERCENT_DATE])
			self.setNodeC(costNode, x, y + liquidHeight + costHeight/2, Color_red)
			self.setNodeS(costNode, cubeSize, costHeight, Shape_cube)
			self.addLabel(costNode, str(costPercent)+'%', Label_top)
			x += cubeDistance

	def addStickGraph(self, dic):
		stickX = 0

		sumsOfHeight = 5 * cubeSize
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
			self.addInfo(stickX,0,key)
			stickX += cubeDistance

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

						marketsSubGraph = self.graph.getSubGraph('Markets')
						subGraphUSA = marketsSubGraph.getSubGraph('USA')
						subGraphHK = marketsSubGraph.getSubGraph('HK')
						subGraphEU = marketsSubGraph.getSubGraph('EU')
						subGraphEU.addNode(tempNode)
						subGraphHK.addNode(tempNode)
						subGraphUSA.addNode(tempNode)

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
		




