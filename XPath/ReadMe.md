### <u> XPath Playground to explore the XPath syntax:</u> <a herf='https://scrapinghub.github.io/xpath-playground/'>Click Here</a>


# Basic XPath Syntax for Web Scraping
- **Selecting All Nodes of a Tag:**
//tagname
<br> **Example:** `//div` - Selects all `<div>` elements.

- **Selecting Nodes with a Specific Attribute**:
//tagname[@attribute='value']
<br> **Example:** `//a[@href='example.com']` - Selects all `<a>` elements with an `href` attribute equal to 'example.com'.

- **Selecting Nodes with a Partial Attribute Value**:
//tagname[contains(@attribute, 'value')]
<br> **Example:** `//a[contains(@href, 'example')]` - Selects all `<a>` elements with an `href` attribute containing 'example'.

- **Selecting Nodes Based on Text Content**:
//tagname[text()='value']
<br> **Example:** `//p[text()='Hello World']` - Selects all `<p>` elements with the exact text 'Hello World'.

- **Selecting Nodes with a Partial Text Content**:
//tagname[contains(text(), 'value')]
<br> **Example:** `//p[contains(text(), 'Hello')]` - Selects all `<p>` elements containing the text 'Hello'.

- **Selecting Nodes Using Multiple Conditions (AND)**:
//tagname[@attribute1='value1' and @attribute2='value2']
<br> **Example:** `//input[@type='text' and @name='username']` - Selects all `<input>` elements with `type='text'` and `name='username'.

- **Selecting Nodes Using Multiple Conditions (OR)**:
//tagname[@attribute1='value1' or @attribute2='value2']
<br> **Example:** `//input[@type='text' or @type='password']` - Selects all `<input>` elements with `type='text'` or `type='password'`.

- **Selecting Child Nodes**:
//parenttag/childtag
<br> **Example:** `//div/p` - Selects all `<p>` elements that are children of `<div>` elements.

- **Selecting Descendant Nodes**:
//ancestor//descendant
<br> **Example:** `//div//a` - Selects all `<a>` elements that are descendants of `<div>` elements.

## **Selecting Nodes by Position**:
- **First Node**:
  ```
  (//tagname)[1]
  ```
  <br> **Example:** `(//div)[1]` - Selects the first `<div>` element.
- **Last Node**:
  ```
  (//tagname)[last()]
  ```
  <br> **Example:** `(//div)[last()]` - Selects the last `<div>` element.
- **Specific Position**:
  ```
  (//tagname)[position()]
  ```
  <br> **Example:** `(//div)[3]` - Selects the third `<div>` element.

## **Selecting Nodes by Attribute Value Starting with a Specific String**:   
```
//tagname[starts-with(@attribute, 'value')]
```

<br> **Example:** `//input[starts-with(@name, 'user')]` - Selects all `<input>` elements with a `name` attribute starting with 'user'.


## **How to get the text of a particular tag:**
This can only happen incase you are doing the /text over the child node
```
//tagname[@attribute='value']/text()    --> works
//article/text()                        --> doesn't work
//article//text()                       --> works and will return all the text of it's child nodes

```
## **Special Characters:**
-   `.`: Specifies the current context should be used (refers to the present node)
-   `..`: Refers to the parent node
-   `*`: A wildcard character that selects all the elements or attributes regardless of the names
-   `@`: select an attribute
-   `()`: Grouping an XPath expression
-   `[n]`: Indicates that a node with index "n" should be selected

<br> **Example**
        `//h2/..` : return the parent of h2 
        `//h2/.` : returns h2 since this is the present node
        `//article/*/text()`: return the text of all the children nodes of article nodes considering the current context


## **Signifcance of / and // in XPATH:**

-   `/`: Select the **children** from the node set on the left side of this character
-   `//`: Specifies that the matching node set should be located at any level within the document

<br>**Example**:  
`//article/h1/text()` 
`//h1`

### Example Usage in Python with lxml

Here’s how you might use some of these XPath expressions in a Python script with the `lxml` library:

```python
from lxml import html
import requests

# Fetch the content
response = requests.get('http://example.com')
tree = html.fromstring(response.content)

# Example XPath queries
all_divs = tree.xpath('//div')
specific_link = tree.xpath('//a[@href="example.com"]')
partial_link = tree.xpath('//a[contains(@href, "example")]')
text_content = tree.xpath('//p[text()="Hello World"]')
partial_text_content = tree.xpath('//p[contains(text(), "Hello")]')
child_elements = tree.xpath('//div/p')
descendant_links = tree.xpath('//div//a')
first_div = tree.xpath('(//div)[1]')
specific_position = tree.xpath('(//div)[3]')
```