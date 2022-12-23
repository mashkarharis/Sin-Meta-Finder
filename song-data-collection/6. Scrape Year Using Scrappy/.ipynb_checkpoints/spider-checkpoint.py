# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:09:52 2022

@author: mashk
"""

import scrapy


class YearSpider(scrapy.Spider):
    name = 'year-spdier'
    start_urls = ['https://www.youtube.com/watch?v=T-GXCAku5Xc']
    
    # name = 'quote-spdier'
    # start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        INFO_STRING_SELECTOR = 'div#info-strings'
        # TEXT_SELECTOR = '.text::text'
        # AUTHOR_SELECTOR = '.author::text'
        # ABOUT_SELECTOR = '.author + a::attr("href")'
        # TAGS_SELECTOR = '.tags > .tag::text'

        yield{
            "resp":response.css(INFO_STRING_SELECTOR).extract()
        }