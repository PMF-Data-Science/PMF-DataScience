# Scrapy spider

[Scrapy]( https://docs.scrapy.org/en/latest/intro/overview.html) is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival. 

Here is college project, spider for scraping data from [CoinGecko](https://www.coingecko.com/en).
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install scrapy and start project. 

```bash
pip install scrapy
scrapy startproject spider_CoinGecko 
```
Project is already installed so you just need to start spider.
```bash
scrapy crawl spider -O data_CoinGecko.csv
```
You can set desired location for your .csv output with command below.
```bash
cd 'path'
```
## License
[Apache-2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
