import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    '''
    def parse(self, response):
        title=response.xpath('//h1/text()').get()
        countries=response.xpath('//td/a/text()').getall()
        
        yield{
            'title':title,
            'countries':countries
        }
    '''
    '''
    def parse(self, response):
        countries= response.xpath('//td/a')

        for country in countries:
            country_name=country.xpath('./text()').get()
            link=country.xpath('./@href').get()

        
            yield{
                'country_name':country_name,
                'link':link
            }
    '''
    def parse(self,response):
        countries=response.xpath('//td/a')
        
        for country in countries:
            country_name=country.xpath('./text()').get()
            link=country.xpath('./@href').get()
            
            #absolute_url=f'https://www.worldometers.info/{link}'
            #absolute_url=response.urljoin(link)
            #yield scrapy.Request(url=absolute_url)
            yield response.follow(url=link,callback=self.parse_country,meta={'country':country_name})

    def parse_country(self,response):
        table=response.xpath('(//table[contains(@class,"table")])[1]')
        rows=table.xpath('./tbody/tr')
        country_name=response.request.meta['country']
        for row in rows:
            year=row.xpath('./td[1]/text()').get()
            population=row.xpath('./td[2]/strong/text()').get()
        
            yield{'country':country_name,
                'year':year,
                  'population':population}


