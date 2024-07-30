'''
Target: https://www.audible.com/search
Task: Implement Pagination | Scrape the book title, author and durtion of the books from the audible(target) website

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options=Options()
options.add_experimental_option('detach',True)
#options.add_argument('--headless')                     --not operating in headless mode
#options.add_argument('--window-size=1920x1080')        --not operating in headless mode    


#starting the chrome driver
driver=webdriver.Chrome(options=options)
driver.maximize_window()

#initializing the website
website='https://www.audible.com/search'

#getting the target website and maximizing the window
driver.get(website) 

#intializign the data structures to capture the title, author and length of book
title=[]
author=[]
duration=[]

#pagination
pagination=driver.find_element(By.XPATH,'//ul[contains(@class,"pagingElements")]')
last_page=pagination.find_elements(By.XPATH,'./li')[-2].text

current_page=1

while current_page<=int(last_page):
    #time.sleep(2)                       #implicit wait
    
    #Explicit Waits
    section=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//div[@class="adbl-impression-container "]')))
    products=WebDriverWait(section,5).until(EC.presence_of_all_elements_located((By.XPATH,'.//li[contains(@class,"productListItem")]')))

    for product in products:
        title.append(product.find_element(By.XPATH,'.//h3[contains(@class,"bc-heading")]').text)
        author.append(product.find_element(By.XPATH,'.//li[contains(@class,"authorLabel")]').text)
        duration.append(product.find_element(By.XPATH,'.//li[contains(@class,"runtimeLabel")]').text)

    #finding the next button
    try:    
        next_button=pagination.find_element(By.XPATH,'//span[contains(@class,"nextButton")]')
        next_button.click()
    except:
        pass
    
    print(f'Page: {current_page} scrapped\n')
    current_page+=1

driver.quit()

#creating a dataframe
df=pd.DataFrame({'title':title,'author':author,'duration':duration})

#exporting the data
df.to_csv('data_dd/audible_allPages_dd.csv',index=False)