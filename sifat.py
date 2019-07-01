import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/home/sifat/scrapping/chromedriver')

browser.get("https://twitter.com/Sah75official")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")#grab whole thing....https://stackoverflow.com/questions/21006940/how-to-load-all-entries-in-an-infinite-scroll-at-once-to-parse-the-html-in-pytho

no_of_pagedowns = 40

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_class_name("js-stream-item")#class defining..where you want to start scrapping 

page = [(post.get_attribute('innerHTML')) for post in post_elems] #genarte a list of html code from webelement 
page = ''.join(page)#convert the list into a string

soup = BeautifulSoup(page,'html.parser')#beautifulsoup object


div= soup.find_all('div','tweet')#scrapping the div where class name is tweet.

attribute = [i.attrs for i in div]#scrape attribute value 


data = [j['data-permalink-path'] for j in attribute]#from that value choose which you want

#save that data into a text file
f = open('log.txt','w')

for i in data:
    f.write('https://twitter.com'+ i + '\n')
f.close()


