
from GetGraphData import GetGraphData
from LayoutInit import LayoutInit
from TimeAnalyse import TimeAnalyse


#==================================================================================================#
#||  Date   ||   Hour   ||  Stock  || Share || Transcation  || Values || money || kind  ||   Sum  ||
#===================================================================================================
#|| 23/2/11 || 12:32:00 ||   IBM   ||  23   ||   "Sold"	 ||  223   ||  USD  || cost  || 232,23 ||
#===================================================================================================
#|| 23/1/13 || 12:32:23 ||   WAG	 ||  23   ||  "Acquired"  ||  23,2  ||  EU   ||income || 332,2  ||
#===================================================================================================

#Matrix := [[year, month, day],Hour,Transcation,Stock,money,Shares,Values,node]


def controlInfo():
	print '1 layout intial'
	print '2 layout daily activity'
	print '3 layout composite'
	print '4 layout income intial'
	print '5 stock buy ratio layout'
	print '6 stocks profits layout'
	print "7 sum of ADM's property"
	print 'A_dd edge'
	print 'C_lear nodes'
	print 'D_elete edges'
	print 'E_mpty subgraphs'
	print 'H_ide nodes'
	print 'L_ables clear'
	print 'S_ubgraphsL:'
	print '    S1: add subgraph of years'
	print '    S2: add subgraph of money kinds'
	print '    S3: add subgraph of transcation'
	print '    S4: add subgraphs of stocks'
	print '       S4D: delete subgraphs of stocks'
	print 'T_ime to get the time percent information.'

def play(graph):

	choice = raw_input('Please make your choice: ')
	choice = choice.upper()
	
	graphData = GetGraphData(graph)
	myMatrix = graphData.getMatrix()
	
	layout1 = LayoutInit(graph)
	myTime = TimeAnalyse(graph, myMatrix)
	
#	print myMatrix[326]
#	print myMatrix[327]
	
	if choice == '1':
		layout1.setLayoutInit(myMatrix)	
		
	elif choice == '2':
		if not graph.getSubGraph('Years'):
			print 'You need add the subgraphs first'
			return 0
		layout1.setLayoutDays(myMatrix)
	elif choice == '3':
		layout1.setLayoutInit2(myMatrix)
	elif choice == '4':
		myProfits = ProfitsAnalyse(myMatrix)
		profitsList = myProfits.getProfitsList()
		profitsLayout = AnalyseLayout(graph)
		profitsLayout.setLayoutIncomeInit(myMatrix,profitsList)	
	elif choice == '5':
		myProfits = ProfitsAnalyse(myMatrix)
		res2 = myProfits.buyStockRatePercent(myMatrix)	
		profitsLayout = AnalyseLayout(graph)
		profitsLayout.costPencentLayout(res2)
	elif choice == '6':
		myProfits = ProfitsAnalyse(myMatrix)
		profitsList = myProfits.getProfitsList()	
		profitsLayout = AnalyseLayout(graph)
		profitsLayout.setLayoutIncomeStick(myMatrix,profitsList)
	elif choice == '7':
		myProfits = ProfitsAnalyse(myMatrix)
		liquideSumList = myProfits.liquidSumList()	
		profitsLayout = AnalyseLayout(graph)
		profitsLayout.setLayoutIncomeStick(myMatrix,liquideSumList, 1)
	elif choice == 'A':
		layout1.addEdge(myMatrix)
	elif choice == 'C':
		layout1.clearNodes()
	elif choice == 'D':
		layout1.clearAllEdges()
	elif choice == 'DA':
		myTime.handingTimeCalcul()
	elif choice == 'E':
		layout1.delSubGraphs()
	elif choice == 'H':
		layout1.makeEspace()
	elif choice == 'L':
		layout1.clearLabel()
	elif choice == 'S1':	
		layout1.addSubgraphEveryYear()
	elif choice == 'S2':
		layout1.addSubgraphDifferentMarket()
	elif choice == 'S3':
		layout1.addSubgraphTransaction()
	elif choice == 'S4':
		layotu1.addSubgraphDifferentStocks()
	elif choice == 'S4D':
		layotu1.deleteSubgraphsOfStocks()
	elif choice == 'T':
		myTime.calHourPercent()
	elif choice == '0':
		print 'Thanks'
	else:
		print 'Wrong input, Please try again!'
		

def writeToFile(StockMatrix):
		myStock.stockMarketInfo()
		searchInfo(myStockMatrix)
		f = open('/Users/REN/Documents/test.txt','w')
		for key in myStockMatrix:
			name = key.split('(')[1].split(')')[0]
			f.write(name + ':')
			f.write(myStockMatrix[key][1])
			f.write('\n')
		file = open('/Users/REN/Documents/SearchResults.txt','r')
		contents = file.readlines()
		for item in contents:	
			print filter(str.isalpha, item)

		myStockMatrix.stockMarketInfo()
			
		file.close()	
	

def main(graph):
	controlInfo()
	play(graph)
	
if __name__ == 'main':
	print 'a'
