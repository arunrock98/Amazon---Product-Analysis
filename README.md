Amazon, an analysis on Electronics
For the current project we were contacted by an international company willing to open a new E-commerce business in EU and with no background with this type of business.
The customer focus was on Electronic products, mainly Laptops, Headphones, Processors, Mouses, Cameras, Monitors...
No sales nor product data were provided by the customer.
Our team had to first focus on knowing the domain in details, understand the business model and then look for appropriate data sources to come up with conlusions and strategies to determine strenghts and weaknesses of this form of business.

Table of contents
Business Understanding
Data Extraction
Data cleaning
Mysql
Tableau
Legal Terms


Business Understanding
E-commerce


E-commerce is the purchasing, selling and exchanging goods and services over computer networks (internet) through which transaction or terms of sale are performed Electronically

Step by step
1 - A consumer uses a web browser to connect to the home page of a merchant‘s Website on the internet.
2 - The consumer browses the catalog of products featured on the site and selects the items to purchase.
3 - When the consumer is ready to complete the purchase, provides a bill-to and ship-to address for purchase and delivery.
4 - Finally the consunmer provides the payment information, cc, and submit the order. Taxes, shipping and handling charges are included in the price.

All considered it seems to be a really easy way of doing business. Let's have now a look at the benefits:

The industry is rapidly growing and it is expected to hit the $5 trillion revenue by this year.
Covid19 has somehow reshaped our world and more consumer have begun shopping online in greater numbers and frequency.
The startup cost are way lower compared to a physical retail store (rent, signs, design, inventory, equipment...)
Ecommerce businesses are open 24H and are easy to access.
The audience they refer to is no longer local but international.
It is easier to collect customer data for analysis.
Opportunity to target the consumers through website personalization and email marketing campaigns.
Ecommerce business are able to process a high number of orders and are easily scalable.
When thinking about Business models are 4 the traditional types:

B2B (Business-to-Business) - The largest form of Ecommerce. Buyer and seller 2 different entities, similar to manufacturer issuing goods to retailer.
B2C (Business-to-Consumer) - In this case the business and the consumer have a direct trade and interaction. The sale of good or services is directly with the final customer.
C2B (Consumer-to-Business) - Exact inverse of the traditional model in which companies offer goods and services to consumers. Eg. The author of a piece of content offers a link to an online business, thus facilitating the purchase of a product (e.g. a book on Amazon.com), for which the author could receive part of the earnings.
C2C (Consumer-to-Consumer) - The opportunity offered by several websites like Ebay to sell unused or redundant stuff online thanks to payment systems like Paypal.

What are the three top Ecommerce businesses in Europe?

1 - Amazon $28 Billion
2 - Otto $12 Billion
3 - John Lewis $7,5 Billion

Data Extraction
Web Scraping
One of best way to know your competitor is to look at what they show publicly on their websites. There are so much informations like product details, prices, customer reviews, product seller information etc. which can help understand the competitor's business in a great extent.
To gather data from websites, we used a technique called Web scraping which is basically a technique of extracting relevant information from websites.



This process can be manual (tedious and redundant) or fully automated thanks to entire ecosystems of multiple tools and libraries built for this extraction process.

The steps for a succesfull Web scraping are the following:

Figure out what is needed to be extracted and locate the information on the webpage.
Send a request to the HTTP or website you are targeting.
The server processes the request and if legitimate we can then read and extract the HTML or CSS of the page
A deep knowledge of HTML is not needed, the foundation will be enough, know what the unique attributes are, ids, classes etc..., navigate the dom (document object model - model or tree of layout for a website, how is the data structured?)
The Information is finally saved in the set variables - Beautifulsoup is the library that can be used for parsing information.
Scraping flow
The following process has been repeated 8 times for 8 different Product types: Processors, Laptops, Cameras, Mouses, Monitors, Headphones, Smartphones, Keyboards.

The first step is to create a txt file (Create search_urls.txt) which will contain all the Urls of the products. Through a for loop I will be able to scrape the website and get all the first 400 Urls (limit declared in the range). The output of this action is to be found in the search_urls.txt
Once all the Urls have been scraped it is time to extract the information about the articles.

Next a yml file is created (search.yml).
This type of language is used for configuration files and in applications where data is being stored or transmitted. In my case it will contain all the element paths from where the informations would be extracted and my goal is to get the components of the articles I am interested in.
I will be looking for multiple information like title, the Url, the rating given from the consumers, the review count and the price of each article.

The search_urls.txt and the search.yml will be then used by the search.py as inputs and will produce as output the search_output.jsonl, a long list of articles with all the components information nested in a json file, and the product_urls.txt containing all urls of the single products for further scraping.

The search.py uses different packages, libraries and file format like:
Selectorlib (a Python package for extracting data from a HTML Page) which will read the yml file and extract the data I marked up on the page.

Requests a Python library used to easily make HTTP requests and getting raw HTML content from websites.

Json (JavaScript Object Notation) is an open standard data format, used for storing and exchanging data.

fake_useragent a library from which we will import UserAgent.

As the article components where not enough for my scope, more information about every article needed to be extracted therefore a products.yml was created to select informations from teh product pages. By looking in the CSS elements of several products I was able to understand where all information where hidden in the text and extract them. For this purpose I installed a chrome extension to use the selector gadget

Next I created the product.py which used the product_urls.txt and products.yml as inputs and gave me as output the product_output.jsonl

Finally the json files where validated with jsonlint and after exporting them to my Visual studio code notebook were ready for the long cleaning process until creatin of 2 csv files ready for further analysis through Mysql.

Data cleaning
The search files were quite easy to clean, they required mainly extracting data from strings, deleting some additional text and changing Data type to the appropriate one.
Extracting the Asin from the Urls required some additional work "cutting" the Urls into pieces and keeping just the value of interest.

The product files instead required a way longer and more complicated journey: when scraping I retrieved all possible data that on the Amazon website appeared to be stored in different tables.
To open this .ipynb please consider using nbviewer and paste the github url in the bar.
When importing this data in my Visual Studio Code notebook I realized how nested it was (Dictionary in dictionary) with several values of interest being stored in the same cells of the df.

Please follow step by step the notebook to see all required steps until data was finally cleaned for my purpose.

This process has been repeated 8 times for 8 different Product types: Processors, Laptops, Cameras, Mouses, Monitors, Headphones, Smartphones, Keyboards. I will here link just the final csv of cleaned data.

Mysql
The cleaned data has been subsequently pushed to Mysql for further analysis - link

To achieve this result I used PyMySQL (here all instructions to install it), an interface for connecting to a MySQL database server from Python. It implements the Python Database API v2. 0 and contains a pure-Python MySQL client library. Other availabale options are MySQL/connector for Python or MySQLdb.

More details about how to create the data source, creating the engine and the connection to Mysql are povided in this Python notebook.

Tableau
Amazon.de - International market

Legal Terms
All data has been used only for educational purpose.