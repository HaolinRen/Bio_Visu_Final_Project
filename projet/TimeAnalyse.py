from MatrixObject import *
from datetime import datetime

class TimeAnalyse(MatrixObject):
	def __init__(self, graph, matrix):
		self.__daysList = self.preProcess(matrix)
		self.graph = graph
		self.Hour = self.graph.getStringProperty('Hour')

	def getDaysList(self):
		return self.__daysList
	
	def calHourPercent(self):
		hourDict = self.getHourInfo()
		hourKeys = hourDict.keys()
		sumHourTimes = 0
		top1Hour = hourKeys[0]
		top2Hour = hourKeys[0]
		top3Hour = hourKeys[0]

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
		def cg(hour):
			 return hour+ ':00 - ' + str(int(hour) + 1) + ':00'
			 
		print 'The most active time of is: %s; %s; %s.'%(cg(top1Hour),cg(top2Hour),cg(top3Hour))
		top1Times = hourDict[top1Hour]
		top2Times = hourDict[top2Hour]
		top3Times = hourDict[top3Hour]

		ratio = float(top1Times + top2Times + top3Times) / sumHourTimes * 100
		print 'They occupy ratio is %s.'%(str(round(ratio))) + '%.'
		return hourDict
	
	def getHourInfo(self, choice = 0):
		timeDict = {}
		for node in self.graph.getNodes():
			if not self.Hour.getNodeValue(node):
				continue
			if choice == 0:
				hourInfo = self.Hour.getNodeValue(node)[0:2]
			else:
				hourInfo = self.Hour.getNodeValue(node)[0:5]
			if hourInfo not in timeDict.keys():
				timeDict[hourInfo] = 1
			else:
				timeDict[hourInfo] += 1
		return timeDict

	#full data
	def diffMethod(self, soldStock, acquiredStock):
		buyTime = acquiredStock[DATE]
		soldTime = soldStock[DATE]
		buyDay = datetime(buyTime[0],buyTime[1],buyTime[2])
		soldDay = datetime(soldTime[0],soldTime[1],soldTime[2])
		dayCount = (soldDay - buyDay).days
		buyDayWeek = buyDay.weekday()
		if dayCount == 3 and buyDayWeek == 4:
			dayCount = 1
		return dayCount
	
	def handingTimeCalcul(self):
		res = {}
		M = len(self.__daysList)
		sumProce = 0
		for daySpace in self.__daysList:
			sumProce += 1
			if daySpace not in res.keys():
				res[daySpace] = 1
			else:
				res[daySpace] += 1
		percent = float(res[1]) / M * 100
		print "1 day handing times: %i, in all %i transactions."%(res[1], sumProce)
		print "The ratio is ",str(percent)[0:4],"% occupied."
