from graphObject import *

ExcutionPhase = {
	1:'Get stock price at day d',
	2: 'Get Variations{d-4,d-3,d-2,d-1}',
	3: 'Call Vector u',
	4: 'Define beta d+1',
	5: 'Ponderate beta With Commission Price',
	6: 'Sort By Best Perfromance',
	7: 'Check Net Liquidity',
	8: 'Define Number Per Share To Buy',
	9: 'Place Limit Order'}
	
learningPhaseLabels = {
	1:'Pick Random Date=d',
	2:'Record Price Variation{d,d1...d5}',
	3:'Creat Vector d->d5',
	4:'Cache Vector',
	5:'Repeat 11e6'}
	
def main(graph): 
	myObject = graphObject(graph)
	myObject.clearNodes()
	myObject.clearAllEdges()
	myObject.makeEspace()
	myObject.clearLabel()
	ExcutionNodeList = []
	learningNodeList = []
	viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")
	viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")
		
	def addExcutionPhase(indiceX,indiceY):
		c1 = 198
		c2 = 195
		c3 = 210
		for index in range(1,10):
			color = tlp.Color(c1,c2,c3)
			tempNode = graph.addNode()
			ExcutionNodeList.append(tempNode)
			myObject.setNodeS(tempNode,1000,120,Shape_cubeOutlined)
			myObject.setNodeC(tempNode,indiceX,indiceY,color)
			myObject.addLabel(tempNode,ExcutionPhase[index],Label_center)
			indiceY -= 180
			c1 -= 10
			c2 -= 10
			
	def beginPhase(indiceX, indiceY):
		node1 = graph.addNode()
		myObject.setNodeS(node1,200,100, Shape_circle)
		myObject.setNodeC(node1,indiceX,indiceY,Color_red)	
		myObject.addLabel(node1,'Begin',Label_center)
		indiceY -= 150
		node2 = graph.addNode()
		myObject.setNodeS(node2,1500,100,Shape_cubeOutlined)
		myObject.setNodeC(node2,indiceX,indiceY,Color_bud)
		info = 'Browse Stock Exchange Components From 2000 to 2013'
		myObject.addLabel(node2,info,Label_center)
		edge1 = graph.addEdge(node1,node2)
		indiceY -= 150
		node3 = graph.addNode()
		myObject.setNodeS(node3,320,100,Shape_circle)
		myObject.setNodeC(node3,indiceX,indiceY,Color_azure)
		myObject.addLabel(node3,'For each',Label_center)
		edge2 = graph.addEdge(node2,node3)
		myObject.viewShape[edge2] = tlp.EdgeExtremityShape.Arrow

	def learningPhase(indiceX,indiceY):
		cindex1 = 200
		cindex2 = 250
		cindex3 = 280
		for index in range(1,6):
			color = tlp.Color(cindex1,cindex2,cindex3)
			node = graph.addNode()
			learningNodeList.append(node)
			myObject.setNodeS(node,700,100,Shape_cubeOutlined)
			myObject.setNodeC(node,indiceX,indiceY,color)
			info = learningPhaseLabels[index]
			myObject.addLabel(node,info,Label_center)
			indiceY -= 160
			cindex1 -= 15
			cindex2 -= 9
			
		node2 = graph.addNode()
		myObject.setNodeS(node2,430,700,Shape_circle)
		myObject.setNodeC(node2,indiceX+800,indiceY+480,Color_red)
		info = 'Neural network'
		myObject.addLabel(node2,info,Label_center)
		edge1 = graph.addEdge(learningNodeList[0],node2)
		edge2 = graph.addEdge(learningNodeList[-1],node2)
		edge3 = graph.addEdge(ExcutionNodeList[2],node2)
		edge4 = graph.addEdge(ExcutionNodeList[3],node2)
		
	def endPhase(indiceX,indiceY):
		node1 = graph.addNode()
		myObject.setNodeS(node1,200,100,Shape_circle)
		myObject.setNodeC(node1,indiceX,indiceY,Color_red)
		myObject.addLabel(node1,'End',Label_center)
		node2 = graph.addNode()
		indiceY -= 200
		myObject.setNodeS(node2,500,100,Shape_circle)
		color = tlp.Color(130,180,100)
		myObject.setNodeC(node2,indiceX,indiceY,color)
		info = 'SELL at d+1'
		myObject.addLabel(node2,info,Label_center)
		indiceY -= 250
		node3 = graph.addNode()
		myObject.setNodeS(node3,200,200,Shape_circle)
		myObject.setNodeC(node3,indiceX,indiceY,Color_azure)
		myObject.addLabel(node3,'BUY',Label_center)
		edge1 = graph.addEdge(node1,node2)
		edge2 = graph.addEdge(node2,node3)
		edge3 = graph.addEdge(ExcutionNodeList[-1],node3)
	
	def addEdges():
		M = len(learningNodeList)
		for index in range(M-1):
			edges = graph.addEdge(learningNodeList[index],learningNodeList[index+1])
			myObject.viewColor[edges] = tlp.Color.Black			
			
		for i in range(2):
			graph.addEdge(ExcutionNodeList[i],ExcutionNodeList[i+1])
		for index in range(3,8):
			edge = graph.addEdge(ExcutionNodeList[index],ExcutionNodeList[index+1])
			myObject.viewColor[edge] = tlp.Color.Black
			
	addExcutionPhase(700,150)
	beginPhase(-300,500)
	learningPhase(-1100,50)
	endPhase(-300,-750)
	addEdges()
	
		
