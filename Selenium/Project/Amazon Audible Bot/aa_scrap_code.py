'''
Target: https://www.audible.com/search
Task: Scrape the book title, author and durtion of the books from the audible(target) website
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

#starting the chrome driver
driver=webdriver.Chrome(options=options)

#initializing the website
website='https://www.audible.com/search'

#getting the target website and maximizing the window
driver.get(website) 
driver.maximize_window()

#subsetting the scraping area
section=driver.find_element(By.XPATH, '//div[@class="adbl-impression-container "]')
products=section.find_elements(By.XPATH,'.//li[contains(@class,"productListItem")]')


#intializign the data structures to capture the title, author and length of book
title=[]
author=[]
duration=[]

for product in products:
    title.append(product.find_element(By.XPATH,'.//h3[contains(@class,"bc-heading")]').text)
    author.append(product.find_element(By.XPATH,'.//li[contains(@class,"authorLabel")]').text)
    duration.append(product.find_element(By.XPATH,'.//li[contains(@class,"runtimeLabel")]').text)


#creating a dataframe
df=pd.DataFrame({'title':title,'author':author,'duration':duration})

#exporting the data
df.to_csv('data_dd/audible_dump.csv',index=False)