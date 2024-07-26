# Notes:

## Basic Packages
1.  There are essentially three packages that can be used to scrape websites.
2.  These **three** packages include:
    - **Beautiful Soup** (great for beginners, only can scrape HTML)
    - **Selenium** (better fit for JS but slow)
    - **Scrapy** (better speed, works for all kinds of websites)

## Ways to export data 
1.  Using the **with** clause.
    ```python
    with open("filename.txt","w") as file:
        file.write("Data is successfully scraped")
    ```

2.  Using the **to_csv** method for Pandas df

## Error Handling methods
1.  Using the **Try and Expect** block
    
    ```python
        try:
        # Attempt to open a file and read its contents
        with open('example.txt', 'r') as file:
            content = file.read()
        except FileNotFoundError as e:
            # Handle the specific case where the file does not exist
            print(f"File not found: {e}")
        except IOError as e:
            # Handle other I/O errors
            print(f"An I/O error occurred: {e}")
        else:
            # If no exception occurs, print the file content
            print("File read successfully:")
            print(content)
        finally:
            # This block runs no matter what, often used for cleanup
            print("Finished file operation.")
    ```

2.  Using the **While and break** construct
    - We use the **While and break** construct when dealing with the limitation of a scraping package
    - For ex. **Pagination**. In Scrapy we can scrap through multiple pages whereas in Selenium and BS we can't. To avoid this we use While and Break statement.

    <br> For example:
    
    ```python 
        # Initialize a counter
        counter = 0

        # Start the while loop
        while True:
            print(f"Counter is at {counter}")
            
            # Increment the counter
            counter += 1
            
            # Check if counter has reached 5
            if counter == 5:
                print("Counter has reached 5, breaking out of the loop.")
                break
    ```

## HTML Tags
        <h1 class="title">Titanic (1997) </h1>
-   h1: tag
-   class: attribute name
-   title: attribute value
-   Titanic (1997): affected content. As this is affected by tag attribute
-   /h1: end tag
**This entire line in called as HTML Element**

### Important HTML Tags and Attributes for Web Scraping

### Important HTML Tags

1. **`<html>`**: The root element of an HTML document.
2. **`<head>`**: Contains meta-information about the HTML document, such as the title, links to stylesheets, and scripts.
3. **`<title>`**: Defines the title of the document, which is displayed in the browser's title bar or tab.
4. **`<body>`**: Contains the contents of an HTML document, such as text, images, links, and other media.
5. **`<div>`**: A container element used to group and style sections of the document.
6. **`<span>`**: An inline container used to group and style parts of text.
7. **`<p>`**: Defines a paragraph.
8. **`<a>`**: Defines a hyperlink, which is used to link from one page to another. The `href` attribute specifies the URL of the linked page.
9. **`<img>`**: Embeds an image in the document. The `src` attribute specifies the path to the image.
10. **`<h1>` to **`<h6>`**: Define HTML headings, with `<h1>` being the highest level and `<h6>` the lowest.
11. **`<ul>` and **`<ol>`**: Define unordered (bulleted) and ordered (numbered) lists, respectively.
12. **`<li>`**: Defines a list item.
13. **`<table>`**: Defines a table.
14. **`<tr>`**: Defines a row in a table.
15. **`<td>`**: Defines a cell in a table.
16. **`<th>`**: Defines a header cell in a table.
17. **`<form>`**: Defines an HTML form for user input.
18. **`<input>`**: Defines an input field within a form.
19. **`<button>`**: Defines a clickable button.
20. **`<script>`**: Embeds a client-side script (e.g., JavaScript).
21. **`<meta>`**: Provides metadata about the HTML document, such as character set and keywords.
22. **`<nav>`**: Used to specify a navigational region such as a pagination bar in a website
23. **`<iframe>`**: This tag makes it possible to embed another page within a page. In HTML5 this is know as nested browsing
24. 

### Important Attributes

1. **`id`**: Specifies a unique identifier for an HTML element.
2. **`class`**: Specifies one or more class names for an HTML element, which can be used for styling and selecting elements.
3. **`name`**: Specifies the name of an HTML element.
4. **`href`**: Specifies the URL of a link.
5. **`src`**: Specifies the source file for an embedded object (e.g., image, script).
6. **`alt`**: Provides alternative text for an image if it cannot be displayed.
7. **`title`**: Specifies extra information about an element (often displayed as a tooltip).
8. **`data-*`**: Used to store custom data private to the page or application.

### Example of Using Tags for Web Scraping

Here is a simple HTML snippet:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample Web Page</title>
</head>
<body>
    <h1 id="main-heading">Welcome to the Sample Page</h1>
    <p class="description">This is a sample web page for web scraping.</p>
    <div id="content">
        <ul>
            <li class="item">Item 1</li>
            <li class="item">Item 2</li>
            <li class="item">Item 3</li>
        </ul>
    </div>
    <a href="https://example.com" id="sample-link">Visit Example</a>
</body>
</html>
```

## Rule of thumb to find an HTML element for scraping

### It is recommended to find elements in this order:
- **ID** (We will always find an element with an ID because they are unique)
- **Class** name
- **Tag** name, CSS Selector
- **Xpath** (Doesn't work with Beautiful Soup)

### Recommended Priority Order to Identify Tree Elements During HTML Web Scraping

When identifying elements in an HTML tree during web scraping, it's important to follow a priority order to ensure that you can reliably and accurately locate the elements you need. Here is a recommended priority order for identifying HTML elements:

#### 1. ID Attribute
- **Priority**: Highest
- **Reason**: IDs are unique within an HTML document, making them the most reliable way to identify elements.
- **Example**: `#main-heading`

#### 2. Class Attribute
- **Priority**: High
- **Reason**: Classes are not unique but can be used to identify groups of elements that share the same styling or purpose. Combine with other attributes or elements for specificity.
- **Example**: `.item`

#### 3. Tag Name with Class or Other Attributes
- **Priority**: Medium
- **Reason**: Sometimes, using a tag name along with a class or other attributes provides enough specificity.
- **Example**: `div.content`, `a[href="https://example.com"]`

#### 4. Hierarchical Selectors (Nested Elements)
- **Priority**: Medium
- **Reason**: Using the structure of the HTML to identify elements can be useful, especially when combined with classes or IDs.
- **Example**: `div#content > ul > li.item`

#### 5. Attribute Selectors
- **Priority**: Medium to Low
- **Reason**: Specific attributes other than ID or class can also be used to locate elements.
- **Example**: `[name="search"]`, `img[alt="Logo"]`

#### 6. Text Content
- **Priority**: Low
- **Reason**: Identifying elements by their text content can be less reliable due to potential changes in the text, but it can be useful in some cases.
- **Example**: `//p[text()='This is a sample web page for web scraping.']` (XPath)

#### 7. Tag Name Alone
- **Priority**: Lowest
- **Reason**: Using only the tag name is the least specific method and should generally be avoided unless combined with other selectors or used within a small, controlled scope.
- **Example**: `p`, `div`


## Different Scraping Mehtods:

-   <u>**Beautiful Soup**</u>
1.  **`find()`**: returns a string element that contains the impacted content of a tag
2.  **`find_all()`**: return a list of all the tags. **The datatype of these list elements is: `bs4.element.Tag`. You can write .get('href') to get a particular attribute of the tag.
3.  **`find_all()`**: You can use `find_all(<attribute>=True)` to find out all the tags which have the value of attribute populated.
4.  

