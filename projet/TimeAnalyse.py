from MatrixObject import *
from datetime import datetime

class TimeAnalyse(MatrixObject):
	def __init__(self, graph, matrix):
		self.__daysList = self.preProcess(matrix)
		self.graph = graph
		self.Hour = self.graph.getStringProperty('Hour')

	def getDaysList(self):
		return self.__daysList

	def hourInfo(self,matrix):
		self.calHourPercent(matrix)
		self.calHourPercent(matrix, 'Sold')
		self.calHourPercent(matrix, 'Acquired','EUR')
		self.calHourPercent(matrix, 'Sold','EUR')
		self.calHourPercent(matrix, 'Acquired','HKD')
		self.calHourPercent(matrix, 'Sold','HKD')

	def calHourPercent(self):
		hourDict = self.__getHourInfo()
		hourKeys = hourDict.keys()
		sumHourTimes = 0
		top1Hour = hourKeys[0]
		top2Hour = hourKeys[0]
		top3Hour = hourKeys[0]
		top4Hour = hourKeys[0]
		top5Hour = hourKeys[0]

		for key in hourKeys:
			sumHourTimes += hourDict[key]
			if hourDict[key] > hourDict[top1Hour]:
				top1Hour = key
			else:
				if hourDict[key] > hourDict[top2Hour]:
					top2Hour = key
				else:
					if hourDict[key] > hourDict[top3Hour]:
						top3Hour = key
					else:
						if hourDict[key] > hourDict[top4Hour]:
							top4Hour = key
						else:
							if hourDict[key] > hourDict[top5Hour]:
								top5Hour = key

		print 'The most active time of is: %s; %s; %s'%(top1Hour,top2Hour,top3Hour,top4Hour,top5Hour)
		ratio = float(top1Times + top2Times + top3Times + top4Hour + top5Hour) / sumHourTimes * 100
		print 'They occupy ratio is %s.'%(str(round(ratio))) + '%.'
		return hourDict
	
	def __getHourInfo(self):
		timeDict = {}
		for node in self.graph.getNodes():
			hourInfo = self.Hour.getNodeValue(node)[0:5]
			if hourInfo not in timeDict.keys():
				timeDict[hourInfo] = 1
			else:
				timeDict[hourInfo] += 1
		return timeDict

	def diffMethod(self, soldStock, acquiredStock):
		buyTime = acquiredStock[DATE]
		soldTime = soldStock[DATE]
		buyDay = datetime(buyTime[0],buyTime[1],buyTime[2])
		soldDay = datetime(soldTime[0],soldTime[1],soldTime[2])
		dayCount = (buyDay - soldDay).days
		buyDayWeek = buyDay.weekday()
		if dayCount == 3 and buyDayWeek == 4:
			dayCount = 1
		print dayCount
		return dayCount
	
	def handingTimeCalcul(self):
		res = {}
		M = len(self.__daysList)
		for daySpace in self.__daysList:
			if daySpace not in res.keys():
				res[daySpace] = 1
			else:
				res[daySpace] += 1

		percent = float(res[1]) / M * 100
		print "1 day handing time: ", res[1]
		print "1 day handing time percent: "
		print "{:10.1f}".format(percent), " %"

				


	
		
