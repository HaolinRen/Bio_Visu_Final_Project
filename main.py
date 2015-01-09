1
from GetGraphData import GetGraphData
from LayoutInit import LayoutInit
from ProfitsProce import ProfitsProce
from StockAnalyse import StockAnalyse
from webContent import *

#==================================================================================================#
#||  Date   ||   Hour   ||  Stock  || Share || Transcation  || Values || money || kind  ||   Sum  ||
#===================================================================================================
#|| 23/2/11 || 12:32:00 ||   IBM   ||  23   ||   "Sold"     ||  223   ||  USD  || cost  || 232,23 ||
#===================================================================================================
#|| 23/1/13 || 12:32:23 ||   WAG	 ||  23   ||  "Acquired"  ||  23,2  ||  EU   ||income || 332,2  ||
#===================================================================================================

#Matrix := [[year, month, day],Hour,Transcation,Stock,money,Shares,Values,node]

def info():
	print '===================================='
	print 'Choose the lettre to excute:'
	print '(1) set to initial layout'
	print '(2) set to days activity layout'
	print '(3) set to profits layout1'
	print '(4) set to profits layout2'
	print '(5) get the information about stocks'
	print '(6) match sotck kinds'
	print '(7) search the stock info from the web'
	print '(A)dd edges'
	print '(C)lear the nodes'
	print '(D)elete edges'
	print '(E)mpty subgraphs'
	print '(L)abel to delete labels'
	print '(S)ubgraphs of years and market'
	print '===================================='

def play(graph):

	choice = raw_input('Please make your choice: ')
	choice = choice.upper()
	
	graphData = GetGraphData(graph)
	myMatrix = graphData.getMatrix()
	
	
	layout1 = LayoutInit(graph)

#	print myMatrix[326]
#	print myMatrix[327]
	
	if choice == '1':
		layout1.setLayoutInit(myMatrix)	
	elif choice == '2':
		layout1.setLayoutDays(myMatrix)
	elif choice == '3':
		profits = ProfitsProce(myMatrix)
		layout1.setLayoutIncomeInit(myMatrix, profits.profitsList)
		profits.netIncome()
	elif choice == '4':
		profits = ProfitsProce(myMatrix)
		layout1.setLayoutIncomeStick(myMatrix, profits.profitsList)
		profits.netIncome()
		marketProfits = profits.diffMarketIncomeYearly(myMatrix)
		for key in marketProfits.keys():
			print key, ': ', marketProfits[key]
	elif choice == '5':
		myStock = StockAnalyse(myMatrix)
		myStockMatrix = myStock.getStockMatrix()
		dic = myStock.getMarketsStockNum()
		print dic
#		for key in dic.keys():
#			print key, ' ,', dic[key][0]/dic[key][1]
#		for item in myStockMatrix.keys():
#			print myStockMatrix[item]
	elif choice == '6':
		myStock = StockAnalyse(myMatrix)
		myStock.stockKinds()
		
	elif choice == '7':
		myStock = StockAnalyse(myMatrix)
		myStockMatrix = myStock.getStockMatrix()
#		searchInfo(myStockMatrix)
#		f = open('/Users/REN/Documents/test.txt','w')
#		for key in myStockMatrix:
#			name = key.split('(')[1].split(')')[0]
#			f.write(name + ':')
#			f.write(myStockMatrix[key][1])
#			f.write('\n')
		file = open('/Users/REN/Documents/SearchResults.txt','r')
		contents = file.readlines()
		for item in contents:	
			print filter(str.isalpha, item)
			
		file.close()
	elif choice == 'A':
		layout1.addEdge(myMatrix)
	elif choice == 'C':
		layout1.clearNodes()
	elif choice == 'D':
		layout1.clearAllEdges()
	elif choice == 'E':
		layout1.delSubGraphs()
	elif choice == 'L':
		layout1.clearLabel()
	elif choice == 'S':	
		layout1.addSubgraphEveryYear()	
		layout1.addSubgraphDifferentMarket()
	elif choice == '0':
		print 'Thanks'
	else:
		print 'Wrong input, Please try again!'
		

def main(graph):
	info()
	play(graph)
	
	
	
	
	

