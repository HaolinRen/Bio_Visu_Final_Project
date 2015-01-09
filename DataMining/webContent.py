
import urllib2
from bs4 import BeautifulSoup
from StockAnalyse import *

def searchInfo(stockKeys):
	for key in stockKeys.keys():
		stockNumber = kye.split('(')[1].split(')')[0]
		if stockKeys[key][STOCK_MONEY] == 'USD':
			searchQuery = stockNumber + ':US'
		elif stockKeys[key][STOCK_MONEY] == 'HKD':
			searchQuery = stockNumber + ':HK'


def serachEnergy(query):
	address = 'http://www.bloomberg.com/quote/%s'%(query)
	req = urllib2.Request(address,headers={'User-Agent':"Magic Browser"})
	resp = urllib2.urlopen(req)
	respHtml = resp.read()
	soup = BeautifulSoup(respHtml)

	firstTag = soup.find('div',class_='exchange_type')
	exchangeTypeTitle = firstTag.find_all('span',class_='l')
	exchangeTypeContents = firstTag.find_all('span',class_=None)
	
	for i in range(4):
		print exchangeTypeTitle[i].get_text(), ': ' exchangeTypeContents[i].get_text()
#print firstTag.find_all('span',class_=None,itemprop=None)
#print soup.find('span',itemprop='exchange').get_text()
#print soup.find_all(attrs={'itemprop':'exchange'}).value

#<div class="exchange_type">
#        <ul>
#          <li>
#            <span class="l">Exchange:</span>
#            <span itemprop="exchange">New York
#            </span>
#          </li>
#          <li>
#            <span class="l">Sector:</span>
#            <span>Financials
#            </span>
#          </li>
#          <li>
#            <span class="l">Industry:</span>
#            <span>Banking
#                
#            </span>
#          </li>
#          <li>
#            <span class="l">Sub-Industry:</span>
#            <span>Banks
#            </span>
#          </li>
#        </ul>
#  </div>