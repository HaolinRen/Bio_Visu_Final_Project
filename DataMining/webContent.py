
import urllib2
from bs4 import BeautifulSoup
from StockAnalyse import *


def searchInfo(stockKeys):
	f = open('/Users/REN/Documents/test.txt','w')
	for key in stockKeys.keys():
		stockNumber = key.split('(')[1].split(')')[0]
		if stockKeys[key][STOCK_MONEY] == 'USD':
			searchQuery = stockNumber + ':US'
			result = searchEnergy(searchQuery)
			f.write(stockNumber)
			f.write('/n')
			f.write(str(result))
		elif stockKeys[key][STOCK_MONEY] == 'HKD':
			searchQuery = stockNumber + ':HK'
			result = searchEnergy(searchQuery)
			f.write(stockNumber)
			f.write('/n')
			f.write(str(result))
	f.close()
	
		
def searchEnergy(query):
	address = 'http://www.bloomberg.com/quote/%s'%(query)
	req = urllib2.Request(address,headers={'User-Agent':"Magic Browser"})
	resp = urllib2.urlopen(req)
	respHtml = resp.read()
	soup = BeautifulSoup(respHtml)
	try:
		firstTag = soup.find('div',class_='exchange_type')
		exchangeTypeTitle = firstTag.find_all('span',class_='l')
		exchangeTypeContents = firstTag.find_all('span',class_=None)
		res = []
		for i in range(4):
			res.append(exchangeTypeTitle[i].get_text() + exchangeTypeContents[i].get_text())
			
	except:
		return 'Unkonw, please check'
	return res
		
#print firstTag.find_all('span',class_=None,itemprop=None)
#print soup.find('span',itemprop='exchange').get_text()
#print soup.find_all(attrs={'itemprop':'exchange'}).value

