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
		calCircle1 = preCircle
		calCircle2 = sedCircle
		result.append(preCircle)
		result.append(sedCircle)
		self.__shellQueue.append(preCircle)
		self.__shellQueue.append(sedCircle)
		
		M = len(sizeList)
		index1 = 0
		for sizeInfo in sizeList[2:M]:
			index2 = 1
			thirdCircle = self.calThirdCircleCord(calCircle1,calCircle2,sizeInfo)
			while not self.testValidCord(thirdCircle, calCircle1):
				calCircle1 = self.__shellQueue[index1]
				if self.testValidTriangle(calCircle1,calCircle2,sizeInfo):
					thirdCircle = self.calThirdCircleCord(calCircle1,calCircle2,sizeInfo)
				if index1 < len(self.__shellQueue):
					index1 += 1
				if index1 == len(self.__shellQueue):
					del self.__shellQueue[0]
					calCircle2 = self.__shellQueue[-index2]
					index2 += 1
					index1 = 0
			
			self.__shellQueue.append(thirdCircle)
			
			result.append(thirdCircle)
			calCircle2 = thirdCircle
		
		return result	
		
	def testDistance(self, circleST, circleRD):
		x1 = circleST[0]
		y1 = circleST[1]
		x2 = circleRD[0]
		y2 = circleRD[1]
		c1 = self.calDist(x1,y1)
		c2 = self.calDist(x2,y2)
		if c2 < c1:
			return False
		else:
			return True
		
	def calDist(self, x1, y1, x2 = 0, y2 = 0):
		return math.sqrt(float(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
		
	def testValidTriangle(self, circleST, circleED, radiusRD):
		x1 = circleST[0]
		y1 = circleST[1]
		r1 = circleST[2]
		x2 = circleED[0]
		y2 = circleED[1]
		r2 = circleED[2]
		C = self.calDist(x1,y1,x2,y2)
		B = r1 + radiusRD
		A = r2 + radiusRD
		if C > A + B or C == 0:
			return False
		else:
			return True

	def testValidCord(self, thirdCircle, calCircle1):
		if not self.testDistance(calCircle1,thirdCircle):
			return False
		for circle in self.__shellQueue:
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
		dist = math.ceil(self.calDist(x1,y1,x2,y2))
		if dist < r1 + r2:
			return False
		else:
			return True

	def calThirdCircleCord(self, circleST, circleED, radiusRD):
		x1 = circleST[0]
		y1 = circleST[1]
		r1 = circleST[2]
		x2 = circleED[0]
		y2 = circleED[1]
		r2 = circleED[2]
		C = self.calDist(x1,y1,x2,y2)
		B = r1 + radiusRD
		A = r2 + radiusRD
		x3 = y3 = 0
		try:
			cosA = float(C*C + B*B - A*A) / (2 * B * C)
		except:
			print "It's not a triangle"
			return 0
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
		