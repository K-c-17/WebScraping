'''
Target Link: https://subslikescript.com/movies
Task: Scrape the Transcript of all the movies listed in the target link

'''

import requests
from bs4 import BeautifulSoup
import time
import re


#defining ciritical functions
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]','',filename)


#defining the website (containing multiple links)
root='https://subslikescript.com'
website=f'{root}/movies'

#getting the website
response=requests.get(website)
content=response.text

#parsing the html using lxml parser
soup=BeautifulSoup(content,'lxml')

#subsetting the scrapped html to relevant areas
box=soup.find('article',class_='main-article')

#collecting the links from the website
links=box.find_all('a',href=True)


#putting all the collected links into a collector list
collector=[]
for link in links:
    collector.append(link['href'])


#transcript dump folder
target='transcript_dd'

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
    


