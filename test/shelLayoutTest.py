import math

#stock numbers = 193
#stock Markets = 6
#stock stock sector = 10
#stock Industry = 34
#stock sub-industry = 74
ExchangeProperties = {
'XRX:US':['NewYork','Technology','TechnologyServices','ITServices'],
'HEN3:GR':['Xetra','ConsumerStaples','ConsumerProducts','HouseholdProducts'],
'APA:US':['NewYork','Energy','Oil,Gas&Coal','Exploration&Production'],
'NWSA:US':['NASDAQGS','Communications','Media','Publishing&Broadcasting'],
'ACA:FP':['ENParis','Financials','Banking','DiversifiedBanks'],
'FRE:GR':['Xetra','HealthCare','HealthCareFacilities&Svcs','HealthCareFacilities'],
'C:US':['NewYork','Financials','Banking','DiversifiedBanks'],
'AVP:US':['NewYork','ConsumerStaples','ConsumerProducts','HouseholdProducts'],
'GLE:FP':['ENParis','Financials','Banking','DiversifiedBanks'],
'GD:US':['NewYork','Industrials','Aerospace&Defense','DefensePrimes'],
'CVX:US':['NewYork','Energy','Oil,Gas&Coal','IntegratedOils'],
'11:HK':['HongKong','Financials','Banking','Banks'],
'CPB:US':['NewYork','ConsumerStaples','ConsumerProducts','PackagedFood'],
'DIS:US':['NewYork','Communications','Media','EntertainmentContent'],
'66:HK':['HongKong','ConsumerDiscretionary','PassengerTransportation','TransitServices'],
'CAP:FP':['ENParis','Technology','TechnologyServices','ITServices'],
'VK:FP':['ENParis','Materials','Iron&Steel','SteelProducers'],
'857:HK':['HongKong','Energy','Oil,Gas&Coal','IntegratedOils'],
'VIE:FP':['ENParis','Utilities','Utilities','UtilityNetworks'],
'QCOM:US':['NASDAQGS','Technology','Semiconductors','SemiconductorDevices'],
'EOA:GR':['-','Utilities','Utilities','Elec&GasMktg&Trading'],
'EXC:US':['NewYork','Utilities','Utilities','IntegratedUtilities'],
'BMY:US':['NewYork','HealthCare','Biotech&Pharma','LargePharma'],
'700:HK':['HongKong','Communications','Media','InternetMedia'],
'2388:HK':['HongKong','Financials','Banking','Banks'],
'WFC:US':['NewYork','Financials','Banking','DiversifiedBanks'],
'DPW:GR':['Xetra','Industrials','Transportation&Logistics','LogisticsServices'],
'KFT:US':['-','ConsumerStaples','ConsumerProducts','PackagedFood'],
'ETR:US':['NewYork','Utilities','Utilities','IntegratedUtilities'],
'2628:HK':['HongKong','Financials','Insurance','LifeInsurance'],
'HON:US':['NewYork','Industrials','ElectricalEquipment','Comml&ResBldgEquip&Sys'],
'494:HK':['HongKong','ConsumerDiscretionary','Distributors-Discretionary','OtherWholesalers'],
'ALO:FP':['ENParis','Industrials','ElectricalEquipment','ElectricalPowerEquipment'],
'UNH:US':['NewYork','HealthCare','HealthCareFacilities&Svcs','ManagedCare'],
'UTX:US':['NewYork','Industrials','Aerospace&Defense','Aircraft&Parts'],
'NKE:US':['NewYork','ConsumerDiscretionary','Apparel&TextileProducts','Apparel,Footwear&AccDesign'],
'XOM:US':['NewYork','Energy','Oil,Gas&Coal','IntegratedOils'],
'GSZ:FP':['ENParis','Utilities','Utilities','PowerGeneration'],
'BNP:FP':['ENParis','Financials','Banking','DiversifiedBanks'],
'RWE:GR':['Xetra','Utilities','Utilities','UtilityNetworks'],
'TGT:US':['NewYork','ConsumerStaples','Retail-ConsumerStaples','MassMerchants'],
'SDF:GR':['Xetra','Materials','Chemicals','AgriculturalChemicals'],
'APC:US':['NewYork','Energy','Oil,Gas&Coal','Exploration&Production'],
'EN:FP':['ENParis','Industrials','Engineering&ConstructionSvcs','InfrastructureConstruction'],
'CL:US':['NewYork','ConsumerStaples','ConsumerProducts','HouseholdProducts'],
'FCX:US':['NewYork','Materials','Metals&Mining','BaseMetals'],
'COST:US':['NASDAQGS','ConsumerStaples','Retail-ConsumerStaples','MassMerchants'],
'HD:US':['NewYork','ConsumerDiscretionary','Retail-Discretionary','HomeProductsStores'],
'GOOG:US':['NASDAQGS','Communications','Media','InternetMedia'],
'MA:US':['NewYork','Financials','SpecialtyFinance','ConsumerFinance'],
'KO:US':['NewYork','ConsumerStaples','ConsumerProducts','Beverages'],
'BAX:US':['NewYork','HealthCare','MedicalEquipment&Devices','HealthCareSupplies'],
'KRFT:US':['NASDAQGS','ConsumerStaples','ConsumerProducts','PackagedFood'],
'DB1:GR':['Xetra','Financials','InstitutionalFinancialSvcs','Security&CmdtyExchanges'],
'CBK:GR':['Xetra','Financials','Banking','Banks'],
'EAD:FP':['-','Industrials','Aerospace&Defense','Aircraft&Parts'],
'EBAY:US':['NASDAQGS','ConsumerDiscretionary','Retail-Discretionary','E-CommerceDiscretionary'],
'ADS:GR':['Xetra','ConsumerDiscretionary','Apparel&TextileProducts','Apparel,Footwear&AccDesign'],
'MT:NA':['ENAmsterdam','Materials','Iron&Steel','SteelProducers'],
'HPQ:US':['NewYork','Technology','Hardware','ComputerHardware&Storage'],
'EMC:US':['NewYork','Technology','Hardware','ComputerHardware&Storage'],
'DCX:GR':['-','ConsumerDiscretionary','Automotive','Automobiles'],
'RNO:FP':['ENParis','ConsumerDiscretionary','Automotive','Automobiles'],
'HEI:GR':['Xetra','Materials','ConstructionMaterials','Cement&Aggregates'],
'MC:FP':['ENParis','ConsumerDiscretionary','Apparel&TextileProducts','Apparel,Footwear&AccDesign'],
'T:US':['NewYork','Communications','Telecom','TelecomCarriers'],
'LHA:GR':['Xetra','ConsumerDiscretionary','PassengerTransportation','Airlines'],
'BHI:US':['NewYork','Energy','Oil,Gas&Coal','Oil&GasServices&Equip'],
'SBUX:US':['NASDAQGS','ConsumerDiscretionary','Gaming,Lodging&Restaurants','Restaurants'],
'MSFT:US':['NASDAQGS','Technology','Software','InfrastructureSoftware'],
'939:HK':['HongKong','Financials','Banking','DiversifiedBanks'],
'BEI:GR':['Xetra','ConsumerStaples','ConsumerProducts','HouseholdProducts'],
'WMB:US':['NewYork','Energy','Oil,Gas&Coal','Midstream-Oil&Gas'],
'1898:HK':['HongKong','Energy','Oil,Gas&Coal','CoalOperations'],
'WAG:US':['-','ConsumerStaples','Retail-ConsumerStaples','Food&DrugStores'],
'BAC:US':['NewYork','Financials','Banking','DiversifiedBanks'],
'SPG:US':['NewYork','Financials','RealEstate','REIT'],
'CS:FP':['ENParis','Financials','Insurance','LifeInsurance'],
'AEP:US':['NewYork','Utilities','Utilities','IntegratedUtilities'],
'DD:US':['NewYork','Materials','Chemicals','SpecialtyChemicals'],
'MCD:US':['NewYork','ConsumerDiscretionary','Gaming,Lodging&Restaurants','Restaurants'],
'17:HK':['HongKong','Financials','RealEstate','RealEstateOwners&Developers'],
'V:US':['NewYork','Financials','SpecialtyFinance','ConsumerFinance'],
'MET:US':['NewYork','Financials','Insurance','LifeInsurance'],
'3:HK':['HongKong','Utilities','Utilities','UtilityNetworks'],
'MDLZ:US':['NASDAQGS','ConsumerStaples','ConsumerProducts','PackagedFood'],
'1088:HK':['HongKong','Energy','Oil,Gas&Coal','CoalOperations'],
'JNJ:US':['NewYork','HealthCare','Biotech&Pharma','LargePharma'],
'293:HK':['HongKong','ConsumerDiscretionary','PassengerTransportation','Airlines'],
'LG:FP':['ENParis','Materials','ConstructionMaterials','Cement&Aggregates'],
'LMT:US':['NewYork','Industrials','Aerospace&Defense','DefensePrimes'],
'CAT:US':['NewYork','Industrials','Machinery','Construction&MiningMachinery'],
'COP:US':['NewYork','Energy','Oil,Gas&Coal','Exploration&Production'],
'EMR:US':['NewYork','Industrials','ElectricalEquipment','IndustrialAutomationControls'],
'ULA:GR':['-','Technology','TechnologyServices','ITServices'],
'MS:US':['NewYork','Financials','InstitutionalFinancialSvcs','InstitutionalBrokerage'],
'SU:FP':['ENParis','Industrials','ElectricalEquipment','ElectricalPowerEquipment'],
'VZ:US':['NewYork','Communications','Telecom','TelecomCarriers'],
'BAS:FP':['-','Financials','Banking','Banks'],
'SAN:FP':['ENParis','HealthCare','Biotech&Pharma','LargePharma'],
'IBM:US':['NewYork','Technology','TechnologyServices','ITServices'],
'AMGN:US':['NASDAQGS','HealthCare','Biotech&Pharma','Biotech'],
'PFE:US':['NewYork','HealthCare','Biotech&Pharma','LargePharma'],
'LOW:US':['NewYork','ConsumerDiscretionary','Retail-Discretionary','HomeProductsStores'],
'S:US':['NewYork','Communications','Telecom','TelecomCarriers'],
'RTN:US':['NewYork','Industrials','Aerospace&Defense','Aircraft&Parts'],
'UNP:US':['NewYork','Industrials','Transportation&Logistics','RailFreight'],
'LLY:US':['NewYork','HealthCare','Biotech&Pharma','LargePharma'],
'BN:FP':['ENParis','ConsumerStaples','ConsumerProducts','PackagedFood'],
'FTE:FP':['-','Communications','Telecom','TelecomCarriers'],
'TWX:US':['NewYork','Communications','Media','EntertainmentContent'],
'FDX:US':['NewYork','Industrials','Transportation&Logistics','CourierServices'],
'MON:US':['NewYork','Materials','Chemicals','AgriculturalChemicals'],
'AA:US':['NewYork','Materials','Metals&Mining','BaseMetals'],
'ORCL:US':['NewYork','Technology','Software','InfrastructureSoftware'],
'TKA:GR':['Xetra','Materials','Iron&Steel','SteelProducers'],
'VOW3:GR':['Xetra','ConsumerDiscretionary','Automotive','Automobiles'],
'DVN:US':['NewYork','Energy','Oil,Gas&Coal','Exploration&Production'],
'COF:US':['NewYork','Financials','SpecialtyFinance','ConsumerFinance'],
'1880:HK':['HongKong','ConsumerDiscretionary','Retail-Discretionary','SpecialtyApparelStores'],
'SO:US':['NewYork','Utilities','Utilities','IntegratedUtilities'],
'PM:US':['NewYork','ConsumerStaples','ConsumerProducts','Tobacco'],
'DTE:GR':['Xetra','Communications','Telecom','TelecomCarriers'],
'330:HK':['HongKong','ConsumerDiscretionary','Retail-Discretionary','SpecialtyApparelStores'],
'386:HK':['HongKong','Energy','Oil,Gas&Coal','IntegratedOils'],
'SLE:US':['-','ConsumerStaples','ConsumerProducts','AgriculturalProducers'],
'BAYN:GR':['Xetra','HealthCare','Biotech&Pharma','LargePharma'],
'GS:US':['NewYork','Financials','InstitutionalFinancialSvcs','InstitutionalBrokerage'],
'MRK:GR':['Xetra','HealthCare','Biotech&Pharma','Biotech'],
'FP:FP':['ENParis','Energy','Oil,Gas&Coal','IntegratedOils'],
'388:HK':['HongKong','Financials','InstitutionalFinancialSvcs','Security&CmdtyExchanges'],
'BA:US':['NewYork','Industrials','Aerospace&Defense','Aircraft&Parts'],
'ACN:US':['NewYork','Technology','TechnologyServices','ITServices'],
'SEV:FP':['ENParis','Utilities','Utilities','UtilityNetworks'],
'INTC:US':['NASDAQGS','Technology','Semiconductors','SemiconductorDevices'],
'WY:US':['NewYork','Financials','RealEstate','REIT'],
'OR:FP':['ENParis','ConsumerStaples','ConsumerProducts','HouseholdProducts'],
'AC:FP':['ENParis','ConsumerDiscretionary','Gaming,Lodging&Restaurants','Lodging'],
'IFX:GR':['Xetra','Technology','Semiconductors','SemiconductorDevices'],
'BK:US':['NewYork','Financials','InstitutionalFinancialSvcs','InstlTrust,Fiduciary&Custody'],
'3328:HK':['HongKong','Financials','Banking','Banks'],
'PG:US':['NewYork','ConsumerStaples','ConsumerProducts','HouseholdProducts'],
'CA:FP':['ENParis','ConsumerStaples','Retail-ConsumerStaples','Food&DrugStores'],
'AXP:US':['NewYork','Financials','SpecialtyFinance','ConsumerFinance'],
'FME:GR':['Xetra','HealthCare','HealthCareFacilities&Svcs','HealthCareFacilities'],
'NSC:US':['NewYork','Industrials','Transportation&Logistics','RailFreight'],
'HAL:US':['NewYork','Energy','Oil,Gas&Coal','Oil&GasServices&Equip'],
'EDF:FP':['ENParis','Utilities','Utilities','PowerGeneration'],
'ML:FP':['ENParis','ConsumerDiscretionary','Automotive','AutoParts'],
'GILD:US':['NASDAQGS','HealthCare','Biotech&Pharma','Biotech'],
'PUB:FP':['ENParis','Communications','Media','Advertising&Marketing'],
'PEP:US':['NewYork','ConsumerStaples','ConsumerProducts','Beverages'],
'GE:US':['NewYork','Industrials','ElectricalEquipment','ElectricalPowerEquipment'],
'CMCSA:US':['NASDAQGS','Communications','Media','Cable&Satellite'],
'SGO:FP':['ENParis','Materials','ConstructionMaterials','NonWoodBuildingMaterials'],
'MRK:US':['NewYork','HealthCare','Biotech&Pharma','LargePharma'],
'1299:HK':['HongKong','Financials','Insurance','LifeInsurance'],
'ABT:US':['NewYork','HealthCare','MedicalEquipment&Devices','LifeScienceEquipment'],
'NOV:US':['NewYork','Energy','Oil,Gas&Coal','Oil&GasServices&Equip'],
'267:HK':['HongKong','Materials','Iron&Steel','SteelProducers'],
'JPM:US':['NewYork','Financials','Banking','DiversifiedBanks'],
'OXY:US':['NewYork','Energy','Oil,Gas&Coal','Exploration&Production'],
'TEC:FP':['ENParis','Energy','Oil,Gas&Coal','Oil&GasServices&Equip'],
'3988:HK':['HongKong','Financials','Banking','Banks'],
'MEO:GR':['Xetra','ConsumerStaples','Retail-ConsumerStaples','Food&DrugStores'],
'DELL:US':['-','Technology','Hardware','ComputerHardware&Storage'],
'UPS:US':['NewYork','Industrials','Transportation&Logistics','CourierServices'],
'2600:HK':['HongKong','Materials','Metals&Mining','BaseMetals'],
'USB:US':['NewYork','Financials','Banking','Banks'],
'ALU:FP':['ENParis','Technology','Hardware','CommunicationsEquipment'],
'CVS:US':['NewYork','ConsumerStaples','Retail-ConsumerStaples','Food&DrugStores'],
'F:US':['NewYork','ConsumerDiscretionary','Automotive','Automobiles'],
'SLB:US':['NewYork','Energy','Oil,Gas&Coal','Oil&GasServices&Equip'],
'UG:FP':['ENParis','ConsumerDiscretionary','Automotive','Automobiles'],
'MO:US':['NewYork','ConsumerStaples','ConsumerProducts','Tobacco'],
'LIN:FP':['ENParis','Technology','Software','InfrastructureSoftware'],
'WMT:US':['NewYork','ConsumerStaples','Retail-ConsumerStaples','MassMerchants'],
'BRK/B:US':['NewYork','Financials','Insurance','P&C;Insurance'],
'KN:FP':['ENParis','Financials','Banking','DiversifiedBanks'],
'EF:FP':['-','HealthCare','MedicalEquipment&Devices','HealthCareSupplies'],
'TXN:US':['NASDAQGS','Technology','Semiconductors','SemiconductorDevices'],
'AMZN:US':['NASDAQGS','ConsumerDiscretionary','Retail-Discretionary','E-CommerceDiscretionary'],
'DOW:US':['NewYork','Materials','Chemicals','Basic&DiversifiedChemicals'],
'MMM:US':['NewYork','Materials','Containers&Packaging','Containers&Packaging'],
'RI:FP':['ENParis','ConsumerStaples','ConsumerProducts','Beverages'],
'CSCO:US':['NASDAQGS','Technology','Hardware','CommunicationsEquipment'],
'23:HK':['HongKong','Financials','Banking','Banks'],
'1398:HK':['HongKong','Financials','Banking','Banks'],
'VIV:FP':['ENParis','Communications','Telecom','TelecomCarriers'],
'PP:FP':['-','ConsumerDiscretionary','Apparel&TextileProducts','Apparel,Footwear&AccDesign'],
'MDT:US':['NewYork','HealthCare','MedicalEquipment&Devices','MedicalDevices'],
'AAPL:US':['NASDAQGS','Technology','Hardware','CommunicationsEquipment'],
'SAP:GR':['Xetra','Technology','Software','ApplicationSoftware'],
}


class ShellAlgorithm(object):
	def __init__(self):
		self.__shellQueue = []

	def getShellCord(self, sizeList):
		result = []
		preSize = sizeList[0]
		preCircle = [0,0,preSize]
		sedSize = sizeList[1]
		radius = sedSize + preSize
		sedCircle = [radius, 0, sedSize]
		calCircle1 = preCircle
		calCircle2 = sedCircle
		result.append(preCircle)
		result.append(sedCircle)
		self.__shellQueue.append(preCircle)
		self.__shellQueue.append(sedCircle)
		
		M = len(sizeList)
		index1 = 0
		for sizeInfo in sizeList[2:M]:
			while not self.testValidTriangle(calCircle1,calCircle2,sizeInfo):
				calCircle2 = self.__shellQueue[index2]
				index2 += 1
			thirdCircle = self.calThirdCircleCord(calCircle1,calCircle2,sizeInfo)
			index2 = 1			
			while not self.testValidCord(thirdCircle, calCircle1):
				calCircle1 = self.__shellQueue[index1]
				if self.testValidTriangle(calCircle1,calCircle2,sizeInfo):
					thirdCircle = self.calThirdCircleCord(calCircle1,calCircle2,sizeInfo)
				if index1 < len(self.__shellQueue):
					index1 += 1
				if index1 == len(self.__shellQueue):
					del self.__shellQueue[0]
					calCircle2 = self.__shellQueue[-index2]
					index2 += 1
					index1 = 0
			
			self.__shellQueue.append(thirdCircle)
			
			result.append(thirdCircle)
			calCircle2 = thirdCircle
		return result	
		
	def testDistance(self, circleST, circleRD):
		x1 = circleST[0]
		y1 = circleST[1]
		x2 = circleRD[0]
		y2 = circleRD[1]
		c1 = self.calDist(x1,y1)
		c2 = self.calDist(x2,y2)
		if c2 < c1:
			return False
		else:
			return True
		
	def calDist(self, x1, y1, x2 = 0, y2 = 0):
		return math.sqrt(float(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
		
	def testValidTriangle(self, circleST, circleED, radiusRD):
		x1 = circleST[0]
		y1 = circleST[1]
		r1 = circleST[2]
		x2 = circleED[0]
		y2 = circleED[1]
		r2 = circleED[2]
		C = self.calDist(x1,y1,x2,y2)
		B = r1 + radiusRD
		A = r2 + radiusRD
		if C > A + B or C == 0 or A > B + C or B > A + C:
			return False
		else:
			return True

	def testValidCord(self, thirdCircle, calCircle1):
		if not self.testDistance(calCircle1,thirdCircle):
			return False
		for circle in self.__shellQueue:
			if not self.isValidCord(thirdCircle, circle):
				return False
		return True
			
	def isValidCord(self, thirdCircle, existCircle):
		x1 = thirdCircle[0]
		y1 = thirdCircle[1]
		r1 = thirdCircle[2]
		x2 = existCircle[0]
		y2 = existCircle[1]
		r2 = existCircle[2]
		dist = round(self.calDist(x1,y1,x2,y2))
		if dist < r1 + r2 or dist == 0:
			return False
		else:
			return True

	def calThirdCircleCord(self, circleST, circleED, radiusRD):
		x1 = circleST[0]
		y1 = circleST[1]
		r1 = circleST[2]
		x2 = circleED[0]
		y2 = circleED[1]
		r2 = circleED[2]
		C = self.calDist(x1,y1,x2,y2)
		B = r1 + radiusRD
		A = r2 + radiusRD
		x3 = y3 = 0
		cosA = float(C*C + B*B - A*A) / (2 * B * C)
		width = x2 - x1
		height = y2 - y1
		degreeAB = 0
		if height < 0:
			if width < 0:
				degreeAB = math.acos(-width / C) + math.pi
			else:
				degreeAB = 2 * math.pi - math.acos(width / C)
		else:
			degreeAB = math.acos(width / C)
		degreeAC = math.acos(cosA) + degreeAB
		x3 = B * math.cos(degreeAC) + x1
		y3 = B * math.sin(degreeAC) + y1

		return [x3, y3, radiusRD]
		
#from textToP_StockInfo import ExchangeProperties
from GetGraphData import *
#from ShellAlgorithm import ShellAlgorithm

#ExchangeProperties = {'ID':['PLACE','SECTOR','INDUSTRY','SubIndustry']}
#propertyMatrix: {name:[[propertyList],[NodeList]]...}
#Tree: [[[propertyList],{name:[node...],name:[...]}]...]

PROP_CITY = 0
PROP_SECTOR = 1
PROP_INDUSTRY = 2
PROP_SUB_INDUSTRY = 3

PROPLIST = 0
NODELIST = 1

class GetPropertyMatrix(GetGraphData):
	def __init__(self, graph):
		self.__sectorsDict = {}
		self.__marketDict = {}
		GetGraphData.__init__(self, graph)
		self.__propertyDict = self.getNameNodeDict()
		self.myShell = ShellAlgorithm()
		
	def getPropertyDict(self):
		return self.__propertyDict

	def getNameNodeDict(self):
		nameNodeDict = {}
		sectorCount = {}
		marketCount = {}
		for node in self.graph.getNodes():
			if not self.Stock.getNodeValue(node):
				continue
			name = self.Stock.getNodeValue(node)
			proList = self.getStockPropertyList(name)
			stockID = proList[0]
			if proList[2] not in sectorCount:
				sectorCount[proList[2]] = 1
			else:
				sectorCount[proList[2]] += 1
			if proList[1] not in marketCount:
				marketCount[proList[1]] = 1
			else:
				marketCount[proList[1]] += 1
			if stockID not in nameNodeDict:
				nameNodeDict[stockID] = [proList[1:],[node]]
			else:
				nameNodeDict[stockID][NODELIST].append(node)
		self.__sectorsDict = sectorCount
		self.__marketDict = marketCount
#		print self.__sectorsDict
#		print self.__marketDict
		return nameNodeDict

	#{name:[propertyList, cord, size]}
	#return [[id,[property list],node,[cord]]...]
	def getShellMatrix(self):
		result = []
		forShellList = []
		for key in self.__propertyDict.keys():
			propertyList = self.__propertyDict[key]
			tempList = [key, propertyList[PROPLIST][1],propertyList[NODELIST][0]]
			times = len(propertyList[NODELIST])
			forShellList.append(times)
			result.append(tempList)
		myShellList = self.myShell.getShellCord(forShellList)
		for index in range(len(result)):
			result[index].append(myShellList[index])
		print 'ADM8 totally buy %i stocks in thoese 4 years.'%(len(result))
		return result

	def stockMarketInfo(self, index):
		stockProperty = []
		for item in ExchangeProperties.keys():
			if ExchangeProperties[item][index] not in stockProperty:
				stockProperty.append(ExchangeProperties[item][index])
		return stockProperty
		
	def stockInfoIntro(self):
		stockProperties = [[],[],[],[]]
		for i in range(4):
			stockProperties[i] = self.stockMarketInfo(i)
		print 'All the stocks all bought from %i stock markets:'%(len(stockProperties[0])-1)
		print stockProperties[0]
		print 'Thoese stocks are in %i sectors:'%(len(stockProperties[1]))
		for i in range(10):
			print i+1,' ',stockProperties[1][i], ', ',
			if i == 5:
				print ''

	def getStockPropertyList(self, stockName):
		res = []
		query = stockName.split('(')[1].split(')')[0]
		if query == 'HEID':
			query = 'HEI'
		elif query == 'MRKK':
			query = 'MRK'
		elif query == 'FP':
			query = 'FP:FP'
		elif ' ' in query:
			query = query.replace(' ','/')
		elif query == 'MT':
			query = 'MT:NA'
		for key in ExchangeProperties.keys():
			if query in key:
				res = [key] + ExchangeProperties[key]
		return res

	def getTreeStruture(self, choice = 0):
		treeDict = []
		for key in ExchangeProperties.keys():
			res = ExchangeProperties[key][choice:]
			if res not in treeDict:
				treeDict.append(res)
		return treeDict

from time import *
from graphObject import *

class PropertyLayout(graphObject):
	def __init__(self,graph):
		graphObject.__init__(self,graph)
	
	# [id,sector,node,[cordx,cordy,size]]
	def stockPropertyLayout(self, propertyList):
		self.clearNodes()		
		self.makeEspace()
		existColor = {}
		flag = False
		for item in propertyList:
			if item[1] not in existColor.keys():
				rColor = self.giveRandomColor()
				existColor[item[1]] = rColor
			else:
				rColor = existColor[item[1]]
				flag = False
			node = item[2]
			x = item[3][0]
			y = item[3][1]
			size = item[3][2] * 2
			self.setNodeC(node,x,y,rColor,2)
			self.setNodeS(node,size,size)
			info = item[0] + ' ' + str(item[3][2])
			self.addLabel(node,info,Label_center)
			sleep(0.05)
			updateVisualization(True)
			
	def addSubgraphOfStockMarkets(self, stockMarketDict):
		if self.graph.getSubGraph('Bourse'):
			return 0
		bourseGraph = self.graph.addSubGraph('Bourse')
		subgraphDict = {}
		
		for item in stockMarketDict.keys():
			bourse = stockMarketDict[item][0][0]
			if bourse not in subgraphDict.keys():
				stockBourse = bourseGraph.addSubGraph(bourse)
				subgraphDict[bourse] = stockBourse
				for node in stockMarketDict[item][1]:
					stockBourse.addNode(node)
			else:
				for node in stockMarketDict[item][1]:
					subgraphDict[bourse].addNode(node)
		else:	
			print 'Subgraph of stock markets added.'
			
#	def addCircleEdge(self, nodeList):
#		M = len(nodeList)
#		if M == 0:
#			return 0
#		for index in range(M - 1):
#			self.graph.addEdge(nodeList[index],nodeList[index+1])
#		
	
	#propertyList = [bourse, sector, industry, subindusty]	
	def treePropertyLayout(self, stockMarketDict, choice = 0):
		self.clearNodes()
		self.clearAllEdges()
		existDict = {}

		bourseNodeDict = {}
		sectorNodeDict = {}
		industryNodeDict = {}
		subIndustyNodeDict = {}

		for key in stockMarketDict.keys():
			oneBourse = stockMarketDict[key]
			propertyList = oneBourse[0]
			nodes = oneBourse[1]
			bourseName = propertyList[0] 
			if bourseName not in existDict.keys():
				bourseNode = self.graph.addNode()
				bourseNodeDict[bourseName] = bourseNode
				existDict[bourseName] = {}
			else:
				sectorName = propertyList[1]
				sectorStr = bourseName + sectorName
				if sectorName not in existDict[bourseName].keys():
					sectorNode = self.graph.addNode()
					self.graph.addEdge(sectorNode,bourseNodeDict[bourseName])
					sectorNodeDict[sectorStr] = sectorNode
					existDict[bourseName][sectorName] = {}
				else:
					industryName = propertyList[2]
					industryStr = sectorStr + industryName
					if industryName not in existDict[bourseName][sectorName].keys():
						industryNode = self.graph.addNode()
						industryNodeDict[industryStr] = industryNode
						self.graph.addEdge(industryNode, sectorNodeDict[sectorStr])
						existDict[bourseName][sectorName][industryName] = {}
					else:
						subIndustryName = propertyList[3]
						subIndustyStr = industryStr + subIndustryName
						if subIndustryName not in existDict[bourseName][sectorName][industryName].keys():
							subIndustryNode = self.graph.addNode()
							self.graph.addEdge(subIndustryNode,industryNodeDict[industryStr])
							subIndustyNodeDict[subIndustyStr] = subIndustryNode
							existDict[bourseName][sectorName][industryName][subIndustryName] = subIndustryNode
							for node in nodes:
								self.graph.addEdge(subIndustryNode,node)
						else:
							subRootNode = existDict[bourseName][sectorName][industryName][subIndustryName]
							for node in nodes:
								self.graph.addEdge(node, subRootNode)

#		self.addCircleEdge(bourseNodeDict.values())
#		self.addCircleEdge(sectorNodeDict.values())
#		self.addCircleEdge(industryNodeDict.values())
#		self.addCircleEdge(subIndustyNodeDict.values())
		print existDict
			
		
def proInfo():
	print 'S_hell Layout of stocks.'
	print "I_nformation of stocks'property"
	

def main(graph):
	myProMatrix = GetPropertyMatrix(graph)
	myPDict = myProMatrix.getNameNodeDict()
	myId = myProMatrix.getPropertyDict()
	sums = 0
	
#	myProMatrix.stockInfoIntro()
#	myShell = myProMatrix.getShellMatrix()
	myLayout = PropertyLayout(graph)
	myLayout.treePropertyLayout(myId)
##	myLayout.stockPropertyLayout(myShell)
