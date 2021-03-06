
from GetGraphData import GetGraphData
from LayoutInit import LayoutInit
from TimeAnalyse import TimeAnalyse
from AnalyseLayout import AnalyseLayout
from ProfitsAnalyse	import ProfitsAnalyse
from GetPropertyMatrix import GetPropertyMatrix

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
	print '2D give the rate of EUR to USD'
	print '3 layout composite'
	print '4 layout income intial'
	print '5 stock buy ratio layout'
	print '6 stocks profits layout'
	print '   Information about most loss stock'
	print "7 sum of ADM's property"
	print '    7D for more property detail'
	print 'A_dd edge'
	print 'C_lear nodes'
	print 'D_elete edges'
	print 'E_mpty subgraphs'
	print 'H_ide nodes'
	print 'H_ading time layout'
	print 'L_ables clear'
	print 'S_ubgraphsL:'
	print '  S1: add subgraph of years'
	print '  S2: add subgraph of money kinds'
	print '  S3: add subgraph of transcation'
	print '  S4: add subgraphs of stocks'
	print '      S4D: delete subgraphs of stocks'
	print 'T_ime to get the time percent information.'

def play(graph):

	choice = raw_input('Please make your choice: ')
	choice = choice.upper()
	
	graphData = GetGraphData(graph)
	myMatrix = graphData.getMatrix()
	layout1 = LayoutInit(graph)
	myTime = TimeAnalyse(graph, myMatrix)
	
	if choice == '1':
		layout1.setLayoutInit(myMatrix)	
	elif choice == '2':
		if not graph.getSubGraph('Years'):
			print 'You need add the subgraphs first'
			return 0
		layout1.setLayoutDays(myMatrix)
	elif choice == '2D':
		sub = graph.getSubGraph('Markets')
		subEU = sub.getSubGraph('EU')
		infoNode = subEU.addNode()
		viewTexture =  graph.getStringProperty("viewTexture")
		layout1.setNodeS(infoNode,530,560)
		color = tlp.Color(255,255,255)
		layout1.viewShape[infoNode] = tlp.NodeShape.Cube
		layout1.setNodeC(infoNode,1200,-500,color)
		viewTexture[infoNode] = 'qq.png'		
		
	elif choice == '3':
		layout1.setLayoutInit2(myMatrix)
	elif choice == '4':
		myProfits = ProfitsAnalyse(myMatrix)
		myProfits.netIncome(1)
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
		myProfits.netIncome()
		myProfits.diffMarketIncomeYearly(myMatrix)
		profitsLayout = AnalyseLayout(graph)
		profitsLayout.setLayoutIncomeStick(myMatrix,profitsList)
	elif choice == 'I6':
		print myMatrix[326][0:5]
		print myMatrix[327][0:5]
		print 'ADM8 bought %i shares.'%(myMatrix[326][5])
		print 'Buy price for each share is: ', str(myMatrix[326][6])[:3]
		print 'Sold price for each share is: ', str(myMatrix[327][6])[:3]
		print 'It lost: %i $.'%(round(myMatrix[326][5]*(myMatrix[326][6]-myMatrix[327][6])))
	elif choice == '7':
		myProfits = ProfitsAnalyse(myMatrix)
		liquideSumList = myProfits.liquidSumList()	
		profitsLayout = AnalyseLayout(graph)
		profitsLayout.setLayoutIncomeStick(myMatrix,liquideSumList, 1)
	elif choice == '7D':
		existDay = myTime.existDays
		print 'The ADM8 has been running %i days losting 1849 $.'%(existDay)
		print 'The orginal money is 11278 $.'
		print 'It would be able to run for 11278 / 1849 * 1155 = %i days'%(round(11278/1519 * existDay))	
		print 'Exchange rate of euro and dollar of 2011.8.31 is 1.36 : 1.'
		print 'It means the start money is 11278 / 1.36 = %i euro'%(round(11278.0/1.36))	
		print 'Exchange rate of euro and dollar of 2014.11.31 is 1.21 : 1.'
		print 'It means ADM own (11278 - 1849) / 1.21 = %i euro.'%(round((11278 - 1849) / 1.21))
		print 'If as the euro to calcule the profits, it would lost 8232 - 7793 = %i euro'%(8232-7793)
		print 'From this, we can calcule it would be running for 8232 / 503 * 1164 = %i days.'%(8232/425 * 1164)
		
	elif choice == 'A':
		layout1.addEdge(myMatrix)
	elif choice == 'C':
		layout1.clearNodes()
	elif choice == 'D':
		layout1.clearAllEdges()
	elif choice == 'E':
		layout1.delSubGraphs()
	elif choice == 'H':
		layout1.makeEspace()
	elif choice == 'HD':
		daysLayout = AnalyseLayout(graph)
		daysList = myTime.getDaysList()
		daysLayout.handingDaysLayout(myMatrix,daysList)
		myTime.handingTimeCalcul()
	elif choice == 'L':
		layout1.clearLabel()
	elif choice == 'S1':	
		layout1.addSubgraphEveryYear()
	elif choice == 'S2':
		layout1.addSubgraphDifferentMarket()
	elif choice == 'S3':
		layout1.addSubgraphTransaction()
	elif choice == 'S4':
		layout1.addSubgraphDifferentStocks()
	elif choice == 'S4D':
		layout1.deleteSubgraphsOfStocks()
	elif choice == 'T':
		hourStickInfo = myTime.getHourInfo()
		layout1.addStickGraph(hourStickInfo, 10000)
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
	print 'This is main.'
