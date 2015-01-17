from time import *
from graphObject import *

class PropertyLayout(graphObject):
	def __init__(self,graph):
		graphObject.__init__(self,graph)
	
	# [id,sector,node,[cordx,cordy,size]]
	def stockPropertyLayout(self, propertyList):
		self.clearNodes()		
		self.makeEspace()
		existColor = {}
		flag = False
		for item in propertyList:
			if item[1] not in existColor.keys():
				rColor = self.giveRandomColor()
				existColor[item[1]] = rColor
			else:
				rColor = existColor[item[1]]
				flag = False
			node = item[2]
			x = item[3][0]
			y = item[3][1]
			size = item[3][2] * 2
			self.setNodeC(node,x,y,rColor,2)
			self.setNodeS(node,size,size)
			info = item[0] + ' ' + str(item[3][2])
			self.addLabel(node,info,Label_center)
			sleep(0.05)
			updateVisualization(True)
			
	def addSubgraphOfStockMarkets(self, stockMarketDict):
		if self.graph.getSubGraph('Bourse'):
			return 0
		bourseGraph = self.graph.addSubGraph('Bourse')
		subgraphDict = {}
		
		for item in stockMarketDict.keys():
			bourse = stockMarketDict[item][0][0]
			if bourse not in subgraphDict.keys():
				stockBourse = bourseGraph.addSubGraph(bourse)
				subgraphDict[bourse] = stockBourse
				for node in stockMarketDict[item][1]:
					stockBourse.addNode(node)
			else:
				for node in stockMarketDict[item][1]:
					subgraphDict[bourse].addNode(node)
		else:	
			print 'Subgraph of stock markets added.'
	
	#propertyList = [bourse, sector, industry, subindusty]	
	def treePropertyLayout(self, stockMarketDict, choice = 0):
		self.clearNodes()
		self.clearAllEdges()
		existDict = {}

		bourseNodeDict = {}
		sectorNodeDict = {}
		industryNodeDict = {}
		subIndustyNodeDict = {}

		for key in stockMarketDict.keys():
			oneBourse = stockMarketDict[key]
			propertyList = oneBourse[0]
			nodes = oneBourse[1]
			bourseName = propertyList[0] 
			if bourseName not in existDict.keys():
				bourseNode = self.graph.addNode()
				bourseNodeDict[bourseName] = bourseNode
				existDict[bourseName] = {}
			else:
				sectorName = propertyList[1]
				sectorStr = bourseName + sectorName
				if sectorName not in existDict[bourseName].keys():
					sectorNode = self.graph.addNode()
					self.graph.addEdge(sectorNode,bourseNodeDict[bourseName])
					sectorNodeDict[sectorStr] = sectorNode
					existDict[bourseName][sectorName] = {}
				else:
					industryName = propertyList[2]
					industryStr = sectorStr + industryName
					if industryName not in existDict[bourseName][sectorName].keys():
						industryNode = self.graph.addNode()
						industryNodeDict[industryStr] = industryNode
						self.graph.addEdge(industryNode, sectorNodeDict[sectorStr])
						existDict[bourseName][sectorName][industryName] = {}
					else:
						subIndustryName = propertyList[3]
						subIndustyStr = industryStr + subIndustryName
						if subIndustryName not in existDict[bourseName][sectorName][industryName].keys():
							subIndustryNode = self.graph.addNode()
							self.addEdge(subIndustryNode,industryNodeDict[industryStr])
							subIndustyNodeDict[subIndustyStr] = subIndustryNode
							existDict[bourseName][sectorName][industryName][subIndustryName] = subIndustryNode
							for node in nodes:
								self.addEdge(subIndustryNode,node)
						else:
							subRootNode = existDict[bourseName][sectorName][industryName][subIndustryName]
							for node in nodes:
								self.graph.addEdge(node, subRootNode)

		self.addCircleEdge(bourseNodeDict.values())
		self.addCircleEdge(sectorNodeDict.values())
		self.addCircleEdge(industryNodeDict.values())
		self.addCircleEdge(subIndustyNodeDict.values())
		print existDict













			