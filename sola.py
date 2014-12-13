import scrapy
import json
from scrapy.selector import Selector
from scrapy.spider import Spider
from items import DoubanItem
from scrapy.exceptions import CloseSpider

class DoubanSpider(Spider):
    name = 'sola'
    allowed_domains = ['book.douban.com']
    start_urls = [
            'http://book.douban.com/tag/%E7%BC%96%E7%A8%8B'
            ]

    def parse(self, response):
        books = []
        sel = Selector(response)
        info = sel.xpath('//li[@class="subject-item"]')
        if len(info) == 0:
            raise CloseSpider('---------------------End Search!---------------')


        f = open('books.data','a')
        for site in info.xpath('div[@class="info"]'):
            book = DoubanItem()
            book['title'] = site.xpath('h2/a/@title').extract()[0].encode('utf-8')
            book['link'] = site.xpath('h2/a/@href').extract()[0].encode('utf-8')
            pub = site.xpath('div[@class="pub"]/text()').extract()[0].encode('utf-8')
            pub = pub.strip().split('/')

            book['author'] = pub[0]
            book['price'] = pub[-1]
            desc = site.xpath('p/text()').extract()
            book['desc'] =  desc[0].encode('utf-8') if (len(desc) != 0) else ''
            print('-----------------lALALALALALA----------------------------------------------')
            print(book['title'])
            print(book['link'])
            print(book['author'])
            print(book['price'])
            print(book['desc'])
            ss = "{'title': '" + book['title'] + "' , " + "'link': '" + book['link'] + "' , " + "'author': '" + book['author'] + "' , " + "'price': '" + book['price'] + "' , " + "'desc': '" + book['desc'] + "'}"
            print ss
            target = json.dumps(ss, ensure_ascii=False)
            print target
            f.write(target+'\n')
            print('-----------------lALALALALALA----------------------------------------------\n\n')
            books.append(book)
            yield book


        f.close()

        site = sel.xpath('//span[@class="next"]/a/@href').extract()[0]
        print('url: ' + response.url)
        print('site: ' + site)
        temp = response.url.split('/')
        new_url = temp[0]
        i = 1
        while i < len(temp)-2:
           new_url += '/' + temp[i]
           i += 1
        new_url += site
        new_url = new_url.encode('utf-8')
        print('url: ' + new_url)
        yield scrapy.Request(new_url, callback=self.parse)