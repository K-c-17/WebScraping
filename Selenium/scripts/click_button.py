'''
Target: https://www.adamchoi.co.uk/overs/detailed
Task: Click on the "All Matches" button
'''

#importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

