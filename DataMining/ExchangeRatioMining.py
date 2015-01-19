import urllib2
from bs4 import BeautifulSoup

def searchEnergy(query):
	resList = []
#	address = 'http://www.freecurrencyrates.com/zh-hans/exchange-rate-history/HKD-USD/%s'%(query)
	address = 'http://www.freecurrencyrates.com/zh-hans/exchange-rate-history/EUR-USD/%s'%(query)

	req = urllib2.Request(address,headers={'User-Agent':"Magic Browser"})
	resp = urllib2.urlopen(req)
	respHtml = resp.read()
	soup = BeautifulSoup(respHtml)
	firstTag = soup.find_all('div',class_='one-month-data-cell')
	for item in firstTag:
		date = item.find('div',class_='one-month-data-date').contents
		rate = item.find('div',class_='one-month-data-rate').contents
		dayString = date[0]
		dayString = dayString.replace('\n','')[-2:]
		rateString = rate[0].replace('\n','')
		res = dayString + ': ' + rateString
		resList.append(res)

	return resList

searchEnergy()
fileWrite = open('/Users/REN/Documents/rateEUR_USDSearchResults.txt','w')

lastYear = 2010
for index in range(2013,2014):
	query = str(index)
	res = searchEnergy(query)
	month = 1
	for item in res:
		if item[:2] == '01' and lastYear == index:
			month += 1
		strList = item.split(':')
		myDict = "'" + query + "."
		fileWrite.write(myDict)
		monthStr = str(month) + '.'
		fileWrite.write(monthStr)
		fileWrite.write(strList[0])
		fileWrite.write("'")
		fileWrite.write(':')
		fileWrite.write(strList[1])
		fileWrite.write(',')
		fileWrite.write('\n')
		lastYear = index

fileWrite.close()


			
