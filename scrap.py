# from bs4 import BeautifulSoup
# import requests

# s = requests.Session()
# page = s.get('https://twitter.com/ImRo45')

# soup = BeautifulSoup(page.content,'html.parser')



# li = soup.find_all('li',class_='js-stream-item')

# div = [i.find('div',class_='tweet').attrs for i in li ]

# data = [j['data-permalink-path'] for j in div]

f = open('log.txt','w')


f.write('a'+'\n'+'b')
f.close()


