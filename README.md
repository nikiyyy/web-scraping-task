# web-scraping-task

1. Before you run the spider, make sure that you have specified a "chromedriver.exe" path inside settings.py on line 17!!!!

"
SELENIUM_DRIVER_EXECUTABLE_PATH = which(r'C:\Users\Niki\Documents\GitHub\web-scraping-task\ShopMango\chromedriver.exe')
"

2.1 To run the spider - make sure you are located inside the first ShopMango folder where scrapy.cfg in located. 

2.2 input the following inside a command prompt or terminal - "scrapy crawl singlepage".
Upon completion of script, a file will be generated outside the first ShopMango folder (where chromedriver.exe is located). the file will be named "ShopMangoData-{date}-{hour}"

Note 1
Some instability my occur after a few consecutive runs of the script. This can avoided by using a proxy or waiting ~5 minutes.

Note 2
Please keep in mind that this is my first time using Scrapy :)
