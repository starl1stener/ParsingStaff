
#### Create project
```
scrapy startproject quotes_spider
cd quotes_spider/
scrapy genspider quotes quotes.toscrape.com
```
#### Run auto Crawl
Run in terminal
```
scrapy crawl quotes
```
Edit settings.py:
```
ROBOTSTXT_OBEY = False
```
#### Collect results to file:
```
scrapy crawl gotstarknames -o items.csv
scrapy crawl gotstarknames -o items.json
scrapy crawl gotstarknames -o items.xml
```
#### Run with console
```
scrapy shell
fetch("http://quotes.toscrape.com/")
```
or
```
scrapy shell 'http://quotes.toscrape.com/'
```
Then:
```
response
response.css('h1::text')
response.xpath('//h1/a/text()').extract()
response.xpath('//h1/a/text()').extract_first()
```
** All elements with class 'tag-item'** :
```
response.xpath('//*[@class="tag-item"]/a/text()').extract()
```


## XPath Syntax
Utility: https://www.freeformatter.com/xpath-tester.html
```
scrapy shell
from scrapy.selector import HtmlXPathSelector
or
from scrapy.selector import Selector
sel = HtmlXPathSelector(text = html_doc)
```
Title:
```
sel.xpath('/html/head/title').extract()
sel.xpath('//title').extract()
```
All text in doc:
```
sel.xpath('//text()').extract()
```
Paragraphs:
```
sel.xpath('/html/body/p').extract()
sel.xpath('//p').extract()
sel.xpath('//p[1]').extract()
sel.xpath('//p')[0].extract()
sel.xpath('//p/text()')[0].extract()
```
Extract Link Href:
```
sel.xpath('//h2/a/@href').extract()
```
