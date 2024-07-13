import scrapy

class productspider(scrapy.Spider):
    name = "productspider"
    start_urls = [f"https://www.flipkart.com/search?q=rope&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={p}" for p in range(1,5)]
    
    def parse(self,response):
        names =  response.css('a.s1Q9rs::text').getall()
        prices =  response.css('div._30jeq3::text').getall()
        ratings =  response.css('div._3LWZlK::text').getall()
        
        for name,price,rate in zip(names,prices,ratings):
            yield{
                'Product' : name.strip(),
                'price' : price.strip(),
                'rating' : rate.strip()
                }