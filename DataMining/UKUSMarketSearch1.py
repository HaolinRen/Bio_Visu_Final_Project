import urllib2
from bs4 import BeautifulSoup


def searchEnergy(query):
	try:
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
	except:
		print query, 'except happens!'
		return 0
			

f = open('/Users/REN/Documents/test.txt','r')
file = open('/Users/REN/Documents/SearchResults.txt','w')
a = f.readlines()

sum = 0
sum1 = 0
for item in a:
	queryList = item.split(':')
	queryKind = queryList[1].replace('\n','')
	query = queryList[0]
	if queryKind == 'HKD':
		searchQuery = query +':HK'
		sum += 1
		result = searchEnergy(searchQuery)
	elif queryKind == 'USD':
		if ' ' in query:
			query = query.replace(' ','/')
		
		searchQuery = query +':US'
		sum1 += 1
		result = searchEnergy(searchQuery)
		if result == 0:
			break
		else:
			file.write(searchQuery+':\n')
			for res in result.keys():
				file.write(res)
				file.write(result[res])
	
print sum, 'sum1'
print sum1, 'sum2'
f.close()
file.close()


	
			
			
			
			
			