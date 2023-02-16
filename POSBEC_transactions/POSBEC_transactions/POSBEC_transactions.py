"""Extract transaction data for POSB Everyday Card from DBS transaction webpage as a csv file. Run the following script
 using 'scrapy crawl creditcard'. Fill in start_urls with the url(s) or file location(s) of the relevant html pages."""

import scrapy
import csv

class CreditcardSpider(scrapy.Spider):
    name = "creditcard"
    allowed_domains = []
    start_urls = []
    
    def parse(self, response): 
        csv_file = open('posbec.csv', 'a')
        writer = csv.writer(csv_file)
        writer.writerow(['date', 'transaction', 'amount'])
        
        for child in response.xpath('//table'):
            for row in child.xpath('tr'):
                if 'Transaction Date' in row.xpath('th//text()').extract():
                    table = child
                    for row in table.xpath('tr'):
                        try:
                            date = row.xpath('td//text()')[0].extract()
                            transaction = row.xpath('td//text()')[1].extract()
                            amount = row.xpath('td//text()')[2].extract()
                            writer.writerow([date, transaction, amount])
                        except IndexError:
                            pass
                    break
                
        csv_file.close()
