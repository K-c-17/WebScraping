'''
Target link: https://subslikescript.com/movies_letter-A
Task:

Caution: Beautiful Soup is not compatible for Pagination and you always have to find a work around in case you want to implement
using Beautiful Soup

'''

#importing the relevant packages
import requests
from bs4 import BeautifulSoup
import re
import time

#defining ciritical functions
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]','',filename)


#defining the website (containing multiple links)
root='https://subslikescript.com'
website=f'{root}/movies_letter-A'

#getting the website
response=requests.get(website)
content=response.text

#parsing the html using lxml parser
soup=BeautifulSoup(content,'lxml')


#pagination
page_section=soup.find('ul',class_='pagination')
pages= page_section.find_all('li', class_='page-item')
last_page=pages[-2].text

#initializing the collector list to store all the links
collector=[]
#creating a transcript dump folder
target='transcript_dd'

for i in range(1,int(last_page)+1):
    if i==3:
        break
    #creating the website name dynamically
    website=f'{root}/movies_letter-A?page={i}'

    #creating a soup
    response=requests.get(website)
    content=response.text
    soup=BeautifulSoup(content,'lxml')

    #subsetting the scrapped html to relevant areas
    box=soup.find('article',class_='main-article')

    #collecting the links from the website
    links=box.find_all('a',href=True)


    #putting all the collected links into a collector list
    for link in links:
        collector.append(link['href'])


    #requesting the collected links and capturing the transcripts
    for link in collector:
        complete_link=f'{root}{link}'                      # making the complete link
        print(complete_link)
        
        response=requests.get(complete_link)
        content=response.text
        soup=BeautifulSoup(content,'lxml')

        box=soup.find('article',class_='main-article')      # subsetting to a particular section

        #extracting specifics from the subsets
        try:
            title=box.find('h1').get_text()
        except:
            title='No Title'
        try:
            plot=box.find('p',class_='plot').get_text()
        except:
            plot='No Plot'
        transcript=box.find('div',class_='full-script').get_text(strip=True,separator='\n')

        #santizing the title
        title=sanitize_filename(title)

        #exporting the transcript into a seperate file
        with open(f'{target}/{title}.txt','w',encoding='utf-8') as file:
            file.write(transcript)
        
        # website has put a cap on number of http requests to avoid DOS
        time.sleep(2)