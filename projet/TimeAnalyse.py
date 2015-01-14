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

	def calHourPercent(self, matrix, trans = 'Acquired', moneyKind = 'USD'):
		hourDict = self.getHourInfo(matrix, trans, moneyKind)
		sumHourTimes = 0
		top1Hour = ''
		top1Times = 0
		top2Hour = ''
		top2Times = 0
		top3Hour = ''
		top3Times = 0

		for key in hourDict.keys():
			sumHourTimes += hourDict[key]
			if hourDict[key] > top1Times:
				top1Times = hourDict[key]
				top1Hour = key
			else:
				if hourDict[key] > top2Times:
					top2Times = hourDict[key]
					top2Hour = key
				else:
					if hourDict[key] > top3Times:
						top3Times = hourDict[key]
						top3Hour = key
		print 'The most %s time of %s is: %s; %s; %s'%(moneyKind, trans,top1Hour,top2Hour,top3Hour)
		print 'They appeared %i; %i; %i times'%(top1Times,top2Times,top3Times)
		ratio = float(top1Times + top2Times + top3Times) / sumHourTimes * 100
		print 'They occupy ratio is %s.'%(str(round(ratio))) + '%.'

	
	def getHourInfo(self):
		timeDict = {}
		for node in self.graph.getNodes():
			hourInfo = self.Hour.getNodeValue(node)[0:5]
			if hourInfo not in timeDict.keys():
				timeDict[hourInfo] = 1
			else:
				timeDict[hourInfo] += 1

		return timeDict

	def __diffMethod(self, soldStock, acquiredStock):
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

	def activeDays(self, matrix):
		res = []
		lastMonth = matrix[0][0][1]
		lastDay = matrix[0][0][2]
		count = 0
		for item in matrix:
			day = item[0][2]
			month = item[0][1]
			P = (month - lastMonth) % 12
			if month == lastMonth and day != lastDay:
				count += 1
				lastDay = day
			elif P == 1:
				res.append(count)
				lastMonth = month
				lastDay = day
				count = 1
			elif P > 1:
				for i in range(P - 1):
					res.append(0)
				


	
		
