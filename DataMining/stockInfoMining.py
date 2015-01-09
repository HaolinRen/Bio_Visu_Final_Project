import urllib2
from bs4 import BeautifulSoup

def searchEnergy(query):
	dit = {}
	address = 'http://www.bloomberg.com/quote/%s'%(query)
	req = urllib2.Request(address,headers={'User-Agent':"Magic Browser"})
	resp = urllib2.urlopen(req)
	respHtml = resp.read()
	soup = BeautifulSoup(respHtml)
	firstTag = soup.find('div',class_='exchange_type')
	exchangeTypeTitle = firstTag.find_all('span',class_='l')
	exchangeTypeContents = firstTag.find_all('span',class_=None)

	for i in range(4):
		key = exchangeTypeTitle[i].get_text()
		res = exchangeTypeContents[i].get_text()
		dit[key] = res
		
	return dit
	
fileRead = open('/Users/REN/Documents/test.txt','r')
fileWrite = open('/Users/REN/Documents/StockSearchResults.txt','w')
ReadInfos = fileRead.readlines()

for item in ReadInfos:
	queryList = item.split(':')
	queryKind = queryList[1].replace('\n','')
	query = queryList[0]

	if queryKind == 'HKD':
		searchQuery = query + ':HK'
		result = searchEnergy(searchQuery)
	elif queryKind == 'USD':
		if ' ' in query:
			query = query.replace(' ','/')
		searchQuery = query +':US'
		result = searchEnergy(searchQuery)
	elif queryKind == 'EUR':
		try:
			if query == 'FRE':
				query = 'FREGR'
			searchQuery = query +':FP'
			result = searchEnergy(searchQuery)
		except:
			try:
				if query == 'HEID':
					query = 'HEI'
				if query == 'MRKK':
					query = 'MRK'
				if query == 'FREGR':
					query = 'FRE'
				searchQuery = query +':GR'
				result = searchEnergy(searchQuery)
			except:
				try:
					searchQuery = query +':NA'
					result = searchEnergy(searchQuery)
				except:
					print searchQuery, 'error happens!'
					break

	fileWrite.write(searchQuery+'\n')
	for item in result.keys():
		key = item.replace(' ','')
		fileWrite.write(key)
		res = result[item].replace(' ', '')
		if res == '\n':
			continue
		fileWrite.write(res)
		
fileWrite.close()
fileRead.close()


	
			
			
			
			
			