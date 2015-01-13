
DATE = 0
HOUR = 1
TRANSACTION = 2
STOCK = 3
MONEY = 4
SHARE = 5
VALUE = 6
NODE = 7
LEN = 8

class MatrixObject(object):
	def __init__(self):
		pass

	def __preProcess(self, matrix):
		diff = []
		alreadySoldList = []
		M = len(matrix)
		for itemIndex in range(M):
			if matrix[itemIndex][TRANSACTION] == "Acquired":
				tempAcquiredStock = matrix[itemIndex]
				acquiredNum = tempAcquiredStock[SHARE]
				for soldIndex in range(itemIndex + 1, M):
					if matrix[soldIndex][STOCK] == tempAcquiredStock[STOCK]:
						if matrix[soldIndex][TRANSACTION] == "Sold":
							if matrix[soldIndex][SHARE] == acquiredNum:
								if soldIndex not in alreadySoldList:
									tempSoldStock = matrix[soldIndex]
									result = self.__diffMethod(tempSoldStock,tempAcquiredStock)
									alreadySoldList.append(soldIndex)
									diff.append(result)
									break
		return diff

	def __diffMethod(self, soldStock, acquiredStock):
		pass

	def clearMatrix(self, matrix):
		for item in matrix:
			k = len(item)
			if k > LEN:
				for i in range(LEN, k):
					del item[-1]
