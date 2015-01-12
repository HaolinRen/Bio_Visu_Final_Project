from MatrixObject import *
from datetime import datetime

class HourGraph(MatrixObject):
	def __init__(self):
		pass

	def hourInfo(self,matrix):
		calHourPercent(matrix)
		calHourPercent(matrix, 'Sold')
		calHourPercent(matrix, 'Acquired','EUR')
		calHourPercent(matrix, 'Sold','EUR')
		calHourPercent(matrix, 'Acquired','HKD')
		calHourPercent(matrix, 'Sold','HKD')

	def calHourPercent(matrix, trans = 'Acquired', moneyKind = 'USD'):
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
		print 'The most %s time is: %s; %s; %s'%(trans,top1Hour,top2Hour,top3Hour)
		print 'They appeared %i; %i; %i times'%(top1Times,top2Times,top3Times)
		ratio = float(top1Times + top2Times + top3Times) / sumHourTimes * 100
		print 'They occupy ratio is %s.'%(str(round(ratio))) + '%.'

	
	def getHourInfo(self, matrix, trans = 'Acquired', moneyKind = 'USD'):
		timeDict = {}
		for item in matrix:
			if item[TRANSCATION] =  trans:
				if item[MONEY] = moneyKind:
					hour = matrix[HOUR][0:5]
					if hour not in timeDict.keys():
						timeDict[hour] = 1
					else:
						timeDict[hour] += 1
		return timeDict

	# def calHandingTime(data):
	# 	M = len(data)
	# 	for index in range(M):
	# 		if data[index][1] == "Acquired":
	# 			buyStock = data[index]
	# 			buyTime = buyStock[0]
	# 			day1 = datetime(buyTime[0],buyTime[1],buyTime[2])
	# 			SoldIndex = index + 1
	# 			day2 = 0
	# 			while SoldIndex < M:
	# 				if data[SoldIndex][2] == buyStock[2]:
	# 					if data[SoldIndex][1] == "Sold":
	# 						sellTime = data[SoldIndex][0]
	# 						day2 = datetime(sellTime[0],sellTime[1],sellTime[2])
	# 						break
	# 				SoldIndex += 1
	# 			if day2 == 0:
	# 				dayCount = 0
	# 			else:
	# 				dayCount = (day2 - day1).days
	# 			weekday = day1.weekday()
	# 			if dayCount == 3 and weekday == 4:
	# 				dayCount = 1 
	# 			buyStock.append(dayCount)
	# 	return data

	# def handingTimeLayout(data):
	# 	baseSize = 10
	# 	numberOfLine = 60
	# 	x1 = 0
	# 	x2 = baseSize 
	# 	y1 = 0
	# 	y2 = 0
	# 	for item in data:
	# 		if item[1] == "Acquired" and len(item) == 7:
	# 			if item[6] > 7:
	# 				item[6] = 7
	# 			y2 = item[6] * baseSize + 1 * baseSize
	# 			if item[6] == 2:
	# 				viewColor[item[5]] = tlp.Color.Blue
	# 			elif item[6] == 1:
	# 				viewColor[item[5]] = tlp.Color.Green
	# 			viewShape[item[5]] = tlp.NodeShape.Square
	# 			viewLayout[item[5]] = tlp.Coord(x1, y1 + y2/2)
	# 			viewSize[item[5]] = tlp.Size(x2,y2,1)
	# 			x1 += baseSize + 2
	# 			if x1 > baseSize * numberOfLine:
	# 				x1 = 0
	# 				y1 -= 50
	# 		else:
	# 			viewShape[item[5]] = tlp.NodeShape.Circle
	# 			viewSize[item[5]] = tlp.Size(1,1,1)
	# 			viewLayout[item[5]] = tlp.Coord(1,1,1)

	# def handingTimeCalcul(data):
	# 	res = {}
	# 	tempres = 0
	# 	for item in data:
	# 		if item[1] == "Acquired" and len(item) == 7:
	# 			if item[6] not in res:
	# 				res[item[6]] = 1
	# 			else:
	# 				res[item[6]] += 1
	# 			tempres += 1
	# 	percent = float(res[1]) / tempres * 100
	# 	print "1 day handing time: ", res[1]
	# 	print "1 day handing time percent: "
	# 	print "{:10.1f}".format(percent), " %"
	# 	return res


	# # firstDay = matrix[DATE][0]		
	# # day1 = datetime(firstDay[0],firstDay[1],firstDay[2])
	
	
		
