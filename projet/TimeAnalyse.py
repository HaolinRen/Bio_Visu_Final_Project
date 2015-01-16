from MatrixObject import *
from datetime import datetime

class TimeAnalyse(MatrixObject):
	def __init__(self, graph, matrix):
		self.__daysList = self.preProcess(matrix)
		self.graph = graph
		self.Hour = self.graph.getStringProperty('Hour')
		startDay = datetime(matrix[0][DATE][0],matrix[0][DATE][1],matrix[0][DATE][2])
		lastDay =  datetime(matrix[-1][DATE][0],matrix[-1][DATE][1],matrix[-1][DATE][2])
		self.existDays = (lastDay - startDay).days

	def getDaysList(self):
		return self.__daysList
	
	def getHourInfo(self):
		hourDict = {}
		for node in self.graph.getNodes():
			if not self.Hour.getNodeValue(node):
				continue
			hour = self.Hour.getNodeValue(node)[0:2]
			hourInfo = hour + ':00 - ' + hour + ':59'
			if hourInfo not in hourDict.keys():
				hourDict[hourInfo] = 1
			else:
				hourDict[hourInfo] += 1

		hourKeys = hourDict.keys()
		sumHourTimes = 0
		hourValues = hourDict.values()
		hourValues.sort()
		top1Hour = hourValues[-1]
		top2Hour = hourValues[-2]
		top3Hour = hourValues[-3]

		for key in hourKeys:
			sumHourTimes += hourDict[key]
			if hourDict[key] == top1Hour:
				top1Hour = key
			elif hourDict[key] == top2Hour:
				top2Hour = key
			elif hourDict[key] == top3Hour:
				top3Hour = key

		def ratio(times):
			res = float(times) / sumHourTimes * 100
			return str(round(res)) + '%'
		
		top1Times = hourDict[top1Hour]
		top2Times = hourDict[top2Hour]
		top3Times = hourDict[top3Hour] 
		print 'The most active times of are:'
		print top1Hour,', ',ratio(top1Times)
		print top2Hour,', ',ratio(top2Times)
		print top3Hour,', ',ratio(top3Times)
		print 'They occupy ratio is %s.'%(ratio(top1Times+top2Times+top3Times))
		
		return hourDict

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
