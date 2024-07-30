'''
Recent versions of Selenium (version 4 and later) include a feature called the WebDriver Manager, 
which can automatically manage and download the appropriate driver for the browser you are using.
'''


from selenium import webdriver
 
# disable auto close
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
website = 'https://www.adamchoi.co.uk/overs/detailed'
driver = webdriver.Chrome(options=options)
driver.get(website)


'''
for Selenium <4 version

from selenium import webdriver

website='https://www.adamchoi.co.uk/overs/detailed'
path=r"C:\Users\kshit\Downloads\chromedriver"

driver=webdriver.Chrome(path)
driver.get(website)

time.sleep(10)
driver.quit()

'''