from MatrixObject import *

class HourGraph(MatrixObject):

	def __init__(self, matrix):
		self.daysList = self.preProcess(matrix)

	def buyTime(self,matrix):
		timeMatrix = self.getHourInfo(matrix)
		HKbuyTime = self.getTimesNum(timeMatrix,0)
		EUbuyTime = self.getTimesNum(timeMatrix,1)
		USAbuyTime = self.getTimesNum(timeMatrix)

	def soldTime(self, matrix):
		timeMatrix = self.getHourInfo(matrix,'Sold')
		HKsoldTime = self.getTimesNum(timeMatrix,0)
		EUsoldTime = self.getTimesNum(timeMatrix,1)
		USAsoldTime = self.getTimesNum(timeMatrix)

	def getTimesNum(self,timeMatrix,marketNumber = 2):
		tempList = []
		res = {}
		for item in timeMatrix[marketNumber]:
			if item not in tempList:
				res[item] = 1
				tempList.append(item)
			else:
				res[item] += 1
		return res
	
	def getHourInfo(self, matrix,info = 'Acquired'):
		TimeMatrix = []
		AmericanTime = []
		EuroTime = []
		HKTime =[]
		for item in matrix:
			if item[TRANSCATION] = info:
				time = self.Hour.getNodeValue(item[NODE])[0:5]
				if item[money] = 'HKD':
					HKTime.append(time)
				elif item[money] = 'EUR':
					EuroTime.append(time)
				else:
					AmericanTime.append(time)

		TimeMatrix.append(AmericanTime)
		TimeMatrix.append(EuroTime)
		TimeMatrix.append(HKTime)

		return TimeMatrix


	
		
