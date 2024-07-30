'''
Target: https://www.adamchoi.co.uk/overs/detailed
Task: Click on the "All Matches" button. Then select "Spain" from the Country dropdown and get all the of match data into a dataframe
'''

#importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

#defining the ChromeOptions
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

#defining the website
website='https://www.adamchoi.co.uk/overs/detailed'

#initializing the driver
driver=webdriver.Chrome(options=options)

#getting the website
driver.get(website)

#finding the element
all_matches_button=driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')

# Scroll the element into view
actions = ActionChains(driver)
actions.move_to_element(all_matches_button).perform()


#clicking on the button
all_matches_button.click()


dropdown=Select(driver.find_element(By.ID,'country'))         #Finding the country dropdown location
dropdown.select_by_visible_text('Spain')                            #selecting Spain from the dropdown
time.sleep(3)                                                       #giving some rendering time for the dropdown values to show up


#Selection from the dropdown

#finding all the list elements
matches=driver.find_elements(By.XPATH,'//tr')

date=[]
home_team=[]
score=[]
away_team=[]

#printing all the rows
for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)                #In XPath indexing starts with 1 and not 0
    home_team.append(match.find_element(By.XPATH,'./td[2]').text)           #In XPath indexing starts with 1 and not 0
    score.append(match.find_element(By.XPATH,'./td[3]').text)               #In XPath indexing starts with 1 and not 0
    away_team.append(match.find_element(By.XPATH,'./td[4]').text)           #In XPath indexing starts with 1 and not 0

#shutting down the chrome driver
driver.quit()

#creating a dataframe
df=pd.DataFrame({'date':date,'home_team':home_team,'score':score,'away_team':away_team})
df.to_csv('dd_dump/spain_football_dd.csv',index=False)