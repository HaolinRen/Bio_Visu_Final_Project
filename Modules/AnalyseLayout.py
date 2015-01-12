from graphObject import *

PERCENT_DATE = 0
PERCENT_COST = 1
PERCETN_PROPER = 2

class AnalyseLayout(graphObject):
	def __init__(self,graph):
		graphObject.__init__(self, graph)
		self.makeEspace()
		
	def costPencentLayout(self, costRateMatrix):
		totalHeight = 100 * cubeSize
		x = y = 0
		for item in costRateMatrix:
			properHeight = totalHeight * item[PERCETN_PROPER]
			costPercent = round(item[PERCENT_COST]*100)
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
		
