from time import *
from graphObject import *
from GetPropertyMatrix import *

def properInfo():
	print '1. My shell Layout'
	print '2. Tree layout include exchange stocks.'
	print '3. Tree layout denpend on sectors.'
	print 'I1 information more detail about exchange bourse.'
	print 'I2 information more detail about stock sectors.'
	print 'C_lear nodes'
	print 'D_elete edges'
	print 'E_mpty subgraphs'
	print 'H_ide nodes'
	print 'L_ables clear'
	print 'S_ubgraphs of differet markets'
	
def play(graph):
	choice = raw_input('Please make your choice: ')
	choice = choice.upper()
	
	myPropertyLayout = PropertyLayout(graph)
	myPropertyMatrix = GetPropertyMatrix(graph)	
	if choice == '1':
		shellMatrix = myPropertyMatrix.getShellMatrix()
		myPropertyLayout.stockPropertyShellLayout(shellMatrix)
	elif choice == '2':
		propDict = myPropertyMatrix.getNameNodeDict()
		myPropertyLayout.treePropertyLayout(propDict)
	elif choice == '3':
		propDict = myPropertyMatrix.getNameNodeDict()
		myPropertyLayout.treePropertyLayout2(propDict)
		myPropertyMatrix.getSectorInfo()	
	elif choice == 'I1':
		myPropertyMatrix.getBourseInfo()
	elif choice == 'I2':
		myPropertyMatrix.stockInfoIntro()
	elif choice == 'C':
		myPropertyLayout.clearNodes()
	elif choice == 'D':
		myPropertyLayout.clearAllEdges()
	elif choice == 'E':
		myPropertyLayout.delSubGraphs()
	elif choice == 'H':
		myPropertyLayout.makeEspace()
	elif choice == 'L':
		myPropertyLayout.clearLabel()
	elif choice == 'S':
		propDict = myPropertyMatrix.getNameNodeDict()
		myPropertyLayout.addSubgraphOfStockMarkets(propDict)
	else:
		print 'Wrong input! Please try again!'
		

def main(graph):
	properInfo()
	play(graph)
	
	
	


class PropertyLayout(graphObject):
	def __init__(self,graph):
		graphObject.__init__(self,graph)
	
	# [id,sector,node,[cordx,cordy,size]]
	def stockPropertyShellLayout(self, propertyList):
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
			updateVisualization()
			
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
	def treePropertyLayout(self, stockMarketDict):
		self.clearNodes()
		self.clearAllEdges()
		existDict = {}

		bourseNodeDict = {}
		sectorNodeDict = {}
		industryNodeDict = {}
		subIndustyNodeDict = {}
		
		def addBourse(bourseName):
			bourseNode = self.graph.addNode()
			color = self.giveRandomColor()
			self.setNodeC(bourseNode,1,1,color)
			self.setNodeS(bourseNode,cubeSize * 5,cubeSize * 5)
			self.addLabel(bourseNode,bourseName,Label_center)
			bourseNodeDict[bourseName] = bourseNode
			existDict[bourseName] = {}
			return bourseNode		
		
		def addSector(sectorName, sectorStr, bourseDict):
			sectorNode = self.graph.addNode()
			color = self.giveRandomColor()
			self.setNodeC(sectorNode,1,1,color)
			self.setNodeS(sectorNode,cubeSize*4,cubeSize*4)
			self.addLabel(sectorNode,sectorName,Label_center)
			self.graph.addEdge(sectorNode,bourseNodeDict[bourseName])
			sectorNodeDict[sectorStr] = sectorNode
			bourseDict[sectorName] = {}
			return sectorNode
		
		def addIndustry(industryName, industryStr,sectorDict):
			industryNode = self.graph.addNode()
			color = self.giveRandomColor()
			self.setNodeC(industryNode,1,1,color)
			self.setNodeS(industryNode,cubeSize*3,cubeSize*3)
			self.addLabel(industryNode,industryName,Label_center)
			industryNodeDict[industryStr] = industryNode
			self.graph.addEdge(industryNode, sectorNodeDict[sectorStr])
			sectorDict[industryName] = {}
			return industryNode
			
		def addSubIndustry(subIndustryName, subIndustryStr,industryDict):
			subIndustryNode = self.graph.addNode()
			color = self.giveRandomColor()
			self.setNodeS(subIndustryNode,cubeSize*2,cubeSize*2)
			self.setNodeC(subIndustryNode,1,1,color)
			self.addLabel(subIndustryNode,subIndustryName)
			self.graph.addEdge(subIndustryNode,industryNodeDict[industryStr])
			subIndustyNodeDict[subIndustryStr] = subIndustryNode
			industryDict[subIndustryName] = subIndustryNode
			return subIndustryNode

		for key in stockMarketDict.keys():
			oneBourse = stockMarketDict[key]
			propertyList = oneBourse[0]
			nodes = oneBourse[1]
			bourseName = propertyList[0]
			sectorName = propertyList[1]
			sectorStr = bourseName + sectorName
			industryName = propertyList[2]
			industryStr = sectorStr + industryName
			subIndustryName = propertyList[3]
			subIndustryStr = industryStr + subIndustryName
			if bourseName not in existDict.keys():
				bourseNode = addBourse(bourseName)
				sectorNode = addSector(sectorName, sectorStr, existDict[bourseName])
				industryNode = addIndustry(industryName, industryStr,existDict[bourseName][sectorName])
				subIndustryNode = addSubIndustry(subIndustryName,subIndustryStr,existDict[bourseName][sectorName][industryName])
				for node in nodes:
					color = self.giveRandomColor()
					self.setNodeC(node,1,1,color)
					self.setNodeS(node,cubeSize,cubeSize,Shape_circle)
					self.graph.addEdge(subIndustryNode,node)
			else:
				if sectorName not in existDict[bourseName].keys():
					sectorNode = addSector(sectorName, sectorStr, existDict[bourseName])
					industryNode = addIndustry(industryName, industryStr,existDict[bourseName][sectorName])
					subIndustryNode = addSubIndustry(subIndustryName,subIndustryStr,existDict[bourseName][sectorName][industryName])
					for node in nodes:
						color = self.giveRandomColor()
						self.setNodeC(node,1,1,color)
						self.setNodeS(node,cubeSize,cubeSize,Shape_circle)
						self.graph.addEdge(subIndustryNode,node)
				else:
					if industryName not in existDict[bourseName][sectorName].keys():
						industryNode = addIndustry(industryName, industryStr,existDict[bourseName][sectorName])
						subIndustryNode = addSubIndustry(subIndustryName,subIndustryStr,existDict[bourseName][sectorName][industryName])
						for node in nodes:
							color = self.giveRandomColor()
							self.setNodeC(node,1,1,color)
							self.setNodeS(node,cubeSize,cubeSize,Shape_circle)
							self.graph.addEdge(subIndustryNode,node)
					else:
						if subIndustryName not in existDict[bourseName][sectorName][industryName].keys():
							subIndustryNode = addSubIndustry(subIndustryName,subIndustryStr,existDict[bourseName][sectorName][industryName])
							for node in nodes:
								color = self.giveRandomColor()
								self.setNodeS(node,cubeSize,cubeSize,Shape_circle)
								self.setNodeC(node,1,1,color)
								self.graph.addEdge(subIndustryNode,node)
						else:
							subRootNode = existDict[bourseName][sectorName][industryName][subIndustryName]
							for node in nodes:
								color = self.giveRandomColor()
								self.setNodeC(node,1,1,color)
								self.setNodeS(node,cubeSize,cubeSize,Shape_circle)
								self.graph.addEdge(node, subRootNode)
								
		self.graph.applyLayoutAlgorithm("Bubble Tree",self.viewLayout)


	def treePropertyLayout2(self, stockMarketDict):
		self.clearNodes()
		self.clearAllEdges()
		existDict = {}

		sectorNodeDict = {}
		industryNodeDict = {}
		subIndustyNodeDict = {}		
		
		def addSector(sectorName):
			sectorNode = self.graph.addNode()
			color = self.giveRandomColor()
			self.setNodeC(sectorNode,1,1,color)
			self.setNodeS(sectorNode,cubeSize*5,cubeSize*5)
			self.addLabel(sectorNode,sectorName,Label_center)
			sectorNodeDict[sectorName] = sectorNode
			existDict[sectorName] = {}
			return sectorNode
		
		def addIndustry(industryName, industryStr,sectorDict):
			industryNode = self.graph.addNode()
			color = self.giveRandomColor()
			self.setNodeC(industryNode,1,1,color)
			self.setNodeS(industryNode,cubeSize*4,cubeSize*4)
			self.addLabel(industryNode,industryName,Label_center)
			industryNodeDict[industryStr] = industryNode
			self.graph.addEdge(industryNode, sectorNodeDict[sectorName])
			sectorDict[industryName] = {}
			return industryNode
			
		def addSubIndustry(subIndustryName, subIndustryStr,industryDict):
			subIndustryNode = self.graph.addNode()
			color = self.giveRandomColor()
			self.setNodeS(subIndustryNode,cubeSize*3,cubeSize*3)
			self.setNodeC(subIndustryNode,1,1,color)
			self.addLabel(subIndustryNode,subIndustryName)
			self.graph.addEdge(subIndustryNode,industryNodeDict[industryStr])
			subIndustyNodeDict[subIndustryStr] = subIndustryNode
			industryDict[subIndustryName] = subIndustryNode
			return subIndustryNode

		for key in stockMarketDict.keys():
			oneBourse = stockMarketDict[key]
			propertyList = oneBourse[0]
			nodes = oneBourse[1]
			sectorName = propertyList[1]
			industryName = propertyList[2]
			industryStr = sectorName + industryName
			subIndustryName = propertyList[3]
			subIndustryStr = industryStr + subIndustryName
		
			if sectorName not in existDict.keys():
				sectorNode = addSector(sectorName)
				industryNode = addIndustry(industryName, industryStr,existDict[sectorName])
				subIndustryNode = addSubIndustry(subIndustryName,subIndustryStr,existDict[sectorName][industryName])
				for node in nodes:
					color = self.giveRandomColor()
					self.setNodeC(node,1,1,color)
					self.setNodeS(node,cubeSize,cubeSize,Shape_circle)
					self.graph.addEdge(subIndustryNode,node)
			else:
				if industryName not in existDict[sectorName].keys():
					industryNode = addIndustry(industryName, industryStr,existDict[sectorName])
					subIndustryNode = addSubIndustry(subIndustryName,subIndustryStr,existDict[sectorName][industryName])
					for node in nodes:
						color = self.giveRandomColor()
						self.setNodeC(node,1,1,color)
						self.setNodeS(node,cubeSize,cubeSize,Shape_circle)
						self.graph.addEdge(subIndustryNode,node)
				else:
					if subIndustryName not in existDict[sectorName][industryName].keys():
						subIndustryNode = addSubIndustry(subIndustryName,subIndustryStr,existDict[sectorName][industryName])
						for node in nodes:
							color = self.giveRandomColor()
							self.setNodeS(node,cubeSize,cubeSize,Shape_circle)
							self.setNodeC(node,1,1,color)
							self.graph.addEdge(subIndustryNode,node)
					else:
						subRootNode = existDict[sectorName][industryName][subIndustryName]
						for node in nodes:
							color = self.giveRandomColor()
							self.setNodeC(node,1,1,color)
							self.setNodeS(node,cubeSize,cubeSize,Shape_circle)
							self.graph.addEdge(node, subRootNode)

		self.graph.applyLayoutAlgorithm("Bubble Tree",self.viewLayout)


		
