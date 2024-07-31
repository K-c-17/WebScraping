# SCRAPY!!

## Documentation of Scrapy is available at: https://docs.scrapy.org/en/latest/intro/tutorial.html

### To get common Scrapy commands write in terminal: `scrapy`

### Essential steps with Scrapy:
-   **To start a Scrapy Project**
1.  Go to your target dir. Run in terminal: `scrapy startproject spider_tutorial`

-   **To generate a spider in your Scrapy Project**
1.  Move inside your <project_dir>. 
    `cd <project_dir>`
2.  Generate the spider with pre-defined template:     `scrapy genspider example example.com`   
    -   <i>Don't put http:// in your url. **example** will be the name of your spider</i>
3.  You can't create spiders with the same names. You have to use different names

-   **Scrapy Framework: Templates**
1.  There are two types of Scrapy Spider: 
    -   **scrapy.Spider**
    -   **CrawlSpider**

#### Working with scrapy.Spider
1.  With scrapy.Spider object we get element with: `reponse`
2.  This is similar to **driver** or **soup** object in **Selenium** and **Beautiful Soup** respectively.
3.  Unlike Selenium we can only find element by XPATH in Scrapy. 
4.  How to do it?
    -   `response.xpath('//tag[@AttributeName="Value"]')`
5.  How to get the elements
    ```
    response.xpath().get()          #return the element text
    reponse.xpath().getall()       #returns a list
    ```
6.  
