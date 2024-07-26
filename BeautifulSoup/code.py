#importing the required packages
from bs4 import BeautifulSoup
import requests

website='https://subslikescript.com/movie/Titanic-120338'

response=requests.get(website)

#getting the content of the website
content=response.text

#parsing the html from the content
soup=BeautifulSoup(content,'lxml')

#printing the soup in a prettified fashion
# print(soup.prettify())

'''
scraping different section of the website
'''

#subsetting to a particular seciton
box=soup.find('article',class_='main-article')

#extracting specifics from the subsets
title=box.find('h1').get_text()
plot=box.find('p',class_='plot').get_text()
transcript=box.find('div',class_='full-script').get_text(strip=True,separator='\n') 

#printing the scraped data
print(title)
print(plot)
print(transcript)

#printing the types of scrapped data
# print(type(title))
# print(type(plot))
# print(type(transcript))


#Exporting the scrapped data
with open(f'{title}.txt','w') as file:
    file.write(transcript)