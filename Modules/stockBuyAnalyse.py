from graphObject import *
import calendar

DATE = 0
HOUR = 1
TRANSACTION = 2
STOCK = 3
MONEY = 4
SHARE = 5
VALUE = 6
NODE = 7
LEN = 8

class ActivityAna(graphObject):
	"""docstring for view Days"""
	def __init__(self,graph):
		graphObject.__init__(self, graph)
		
	def getActiveDays(self):
		lastDay = ''
		days = 0
		for node in self.graph.getNodes():
			if not self.Stock.getNodeValue(node):
				continue
			today = self.Date.getNodeValue(node)
			if today != lastDay:
				days += 1
				lastDay = today
		return days
			
def main(graph):
	myAna = ActivityAna(graph)
	ACDays = myAna.getActiveDays()


