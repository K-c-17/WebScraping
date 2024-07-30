# SELENIUM

- <h2>Definiton</h2>
1.  It allows us to scrape website that are created with **JavaScript.**
2.  Therefore it allows us to scrape website with **dynamic content**

- <h2>How to identify that a website runs JS?<br></h2>
    `Webpage >> Inspect >> Settings >> Preferences >> Disable JS`
    <br> If by doing this your website stops rendering post refresh then that mean it runs JS.

- <h2>To use Selenium you need a Chrome Driver<br></h2>
    **ChromeDriver** is a separate executable that Selenium WebDriver uses to control the Chrome browser. 
    Essentially, ChromeDriver **acts as a bridge between Selenium and the Chrome browser**, allowing Selenium to send 
    commands to Chrome and receive responses.

- <h2>Driver:<br></h2>
    In Selenium we use **Driver** to get objects. This is similar to soup object in BeautifulSoup. However, Driver can help us in extracting object of **websites that run Javascript**
    
<h2>Locating Elements in Selenium</h2>

1. In Selenium, we can locate elements by **ID, name, XPath, CSS Selector, etc.**

2. For example, to locate an element with ID:
   ```python
   driver.find_element(By.ID, 'id')
   driver.find_element(By.CLASS_NAME, 'class_name')
    ```
3.  To find element by **XPath** we do:<br> `driver.find_element(By.XPATH, '//tag[@AttributeName="Value"]')`
4.  Other ways to find elements in selenium:
    ```
    driver.find_element(By.CSS_SELECTOR, 'css_selector')
    driver.find_element(By.NAME, 'name')
    driver.find_element(By.LINK_TEXT, 'link_text')
    ```
5.  To find **multiple element names** in Selenium:<br>
    `driver.find_elements(By.CLASS_NAME, 'class_name')   ---> This returns a list of all the elements having the same class name `
6.  Other things that we can locate with Selenium:
-   **Dropdowns**
-   **Login**
-   **Waits**

<h2>How to scroll a webpage incase your target element is hidden by some advertisement:</h2>

-   **Even though an element is tracked in Selenium using the XPath, it's the browser that can't access that element (for clicking) in case it is covered by some adversting iframe. Hence, it is necessary to scroll so as to expose the element so that your chrome driver can easily click on the desired element**

-    **ActionChains are a way to automate low level interactions such as mouse movements, mouse button actions, key press, and context menu     interactions. This is useful for doing more complex actions like hover over and drag and drop.**<br>
-    **When you call methods for actions on the ActionChains object, the actions are stored in a queue in the ActionChains object. When you call perform(), the events are fired in the order they are queued up.**

```
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

menu = driver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
```

<h2>Implicit Vs Explicit Waits:</h2>

-   One drawback of scrapping JS websites using Selenium is that data is loaded dynamically during scrapping
-   This can cause some delay in rendering the webpages as a result an element might not be present when scrapping data
-   Due to this we might encounter **element not visibile** exception
-   This is why we need to make the driver **wait unitl the data is loaded completely on the wepage**

-   **Implicit Wait:** This  tells the browser to wait for a specific time duration when trying to locate an element
                    For eg. time.sleep(10)
-   **Explicit Wait:** This tells the ChromeDriver to wait unitl a certain event occurs.
                    For eg. WebDriverWait(driver,10).until(....)
-   **WebDriverWait(driver,10).until(....)** here if after 10secs the condition inside the unit() block is not satisfied then the code is going to break
-   **unitl(...)**: A very common condition written inside until is `EC.presence_of_element_located(....)`. This waits till a specific element can be located by the ChromeDriver
-   Here is the complete syntax of **EXPLICIT WAIT**: <br>
    `WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"value")))`
-   **Libraries to be imported for this**:
    
    ```
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    ```




    