from graphObject import *

PERCENT_DATE = 0
PERCENT_COST = 1
PERCENT_PROPER = 2

class AnalyseLayout(graphObject):
	def __init__(self,graph):
		graphObject.__init__(self, graph)
		
	def costPencentLayout(self, costRateMatrix):
		self.makeEspace()
		self.clearNodes()
		x = y = 0
		for item in costRateMatrix:
			properHeight = cubeSize * item[PERCENT_PROPER]
			costHeight = properHeight * item[PERCENT_COST] / 100
			liquidHeight = properHeight - costHeight
			costNode = self.graph.addNode()
			liquideNode = self.graph.addNode()
			self.setNodeC(liquideNode, x, y + liquidHeight/2, Color_green)
			self.setNodeS(liquideNode, cubeSize, liquidHeight, Shape_cube)
			self.addLabel(liquideNode, item[PERCENT_DATE])
			self.setNodeC(costNode, x, y + liquidHeight + costHeight/2, Color_red)
			self.setNodeS(costNode, cubeSize, costHeight, Shape_cube)
			self.addLabel(costNode, str(item[PERCENT_COST])+'%', Label_top)
			x += cubeDistance

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

	def setLayoutIncomeStick(self, matrix, dataList, choice = 0):
		x = y = 0
		index = 0
		for item in matrix:
			if item[TRANSACTION] == "Acquired":
				if index < len(dataList):
					if choice == 0:
						nodeInfo = str(dataList[index]) + item[STOCK]
						sizeStick = dataList[index]
						y = sizeStick / 2
						self.setNodeC(item[NODE], x, y, Color_green)
					else:
						nodeInfo = str(int(dataList[index]))
						sizeStick = dataList[index] / 50
						y = 0
						self.setNodeC(item[NODE], x, y + sizeStick/2, Color_green)
					
					self.setNodeS(item[NODE], 1, sizeStick, Shape_cubeOutlined)
					self.addLabel(item[NODE], nodeInfo, Label_top)
				else:
					self.setNodeS(item[NODE])
					self.setNodeC(item[NODE])
				index += 1
				x += 1
			else:
				self.setNodeC(item[NODE])
				self.setNodeS(item[NODE])