import math

class ShellAlgorithm(object):
	def __init__(self):
		self.__shellQueue = []

	def getShellCord(self, sizeList):
		result = []
		preSize = sizeList[0]
		preCircle = [0,0,preSize]
		sedSize = sizeList[1]
		radius = sedSize + preSize
		sedCircle = [radius, 0, sedSize]
		calCircle1 = [x for x in preCircle]
		calCircle2 = [x for x in sedCircle]
		result.append(preCircle)
		result.append(sedCircle)
		self.__shellQueue.append(preCircle)
		self.__shellQueue.append(sedCircle)
		
		M = len(sizeList)
		for sizeInfo in sizeList[2:M]:
			thirdCircle = self.calThirdCircleCord(calCircle1,calCircle2,sizeInfo)
			while not self.testValidCord(thirdCircle):
				del self.__shellQueue[0]
				calCircle1 = [x for x in self.__shellQueue[0]]
				calCircle2 = [x for x in self.__shellQueue[-1]]
				thirdCircle = self.calThirdCircleCord(calCircle1,calCircle2,sizeInfo)
				if len(self.__shellQueue) == 0:
					return 0
			validCircle = [x for x in thirdCircle]
			self.__shellQueue.append(thirdCircle)
			result.append(validCircle)
			calCircle2 = [x for x in thirdCircle]
			
		return result

	def testValidCord(self, thirdCircle):
		for circle in self.__shellQueue:
#			print self.__shellQueue
#			print thirdCircle,' ,' ,circle,' : ', self.isValidCord(thirdCircle, circle)
			if not self.isValidCord(thirdCircle, circle):
				return False
		return True
			
	def isValidCord(self, thirdCircle, existCircle):
		x1 = thirdCircle[0]
		y1 = thirdCircle[1]
		r1 = thirdCircle[2]
		x2 = existCircle[0]
		y2 = existCircle[1]
		r2 = existCircle[2]
		
		dist = math.ceil(math.sqrt(float(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)))
		
		if dist < r1 + r2:
			return False
		else:
			return True

	def calThirdCircleCord(self, circleST, circleED, radiusRD):
		print circleST,' ',circleED
		x1 = circleST[0]
		y1 = circleST[1]
		r1 = circleST[2]
		x2 = circleED[0]
		y2 = circleED[1]
		r2 = circleED[2]
		C = math.sqrt(float(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
		B = r1 + radiusRD
		A = r2 + radiusRD
		x3 = y3 = 0

		cosA = float(C*C + B*B - A*A) / (2 * B * C)
		
		width = x2 - x1
		
		height = y2 - y1
		degreeAB = 0

		if height < 0:
			if width < 0:
				degreeAB = math.acos(-width / C) + math.pi
			else:
				degreeAB = 2 * math.pi - math.acos(width / C)
		else:
			degreeAB = math.acos(width / C)

		degreeAC = math.acos(cosA) + degreeAB
		x3 = B * math.cos(degreeAC) + x1
		y3 = B * math.sin(degreeAC) + y1

		return [x3, y3, radiusRD]
		
testList = [2,3,3,6,3,21,14,34,3,4]

myShell = ShellAlgorithm()
print myShell.getShellCord(testList)
#print myShell.calThirdCircleCord([5,0,3],[-7.418,2.997,6],88)