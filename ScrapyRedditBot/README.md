Creating Reddit parse bot using Scrapy

## Steps:
```
scrapy startproject reddit
scrapy genspider picture www.reddit.com
scrapy crawl --nolog picture
scrapy crawl -o data.csv -t csv --nolog picture
```
