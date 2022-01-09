import scrapy
from scrapy_selenium import SeleniumRequest
from time import strftime
#scrapy_selenium is used because most of the site is dynamically generated
#strftime is used to give a unique file name to the output

#some instability my occur after a few runs of the spider
#this can avoided by using a proxy or waiting ~5 minutes

class ShopMango(scrapy.Spider):
    
    name = "singlepage"
    start_urls = ['https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99']

    def parse(self, response):
        # checks if there is a captcha
        if response.css('#captchacharacters').extract_first():
            print("Captcha found")
            
        url = "https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"
        yield SeleniumRequest(url=url, callback=self.parse_result)


    def parse_result(self,response):
        #if instability occurs, an error will be avoided
        try:
            #name
            prodName = response.css('h1.product-name::text').get()
            #color
            prodColor = response.css('span.colors-info-name::text').get()
            #price
            prodPrice = response.xpath('/html/body/div[5]/div/form/div[2]/div[1]/main/div/div[3]/div[1]/div[2]/span[4]').get()
            prodPrice = prodPrice.replace(">", " ").replace("<", " ").split()[3][3:]
            #size
            prodSize = response.css('div.selector-list').get()
            prodSize = [x[11:-1] for x in prodSize.split() if x.startswith("data-size")]    
            
            #due to the low complexity of the data, I will use a multilevel comment instead of the JSON library, to avoid unnecessary imports 
            data = """
"name": {}
"price": {},
"color": {},
"size": {}
""".format(prodName,prodPrice,prodColor,prodSize)
        except AttributeError:
            print("Captcha found. Please try again later or use proxy")
            data="Captcha found. Please try again later or use proxy"
            
        with open("ShopMangoData-{}.txt".format(strftime("%Y%m%d-%H%M%S")), "w") as f:
            f.write("{"+data+"}")
        