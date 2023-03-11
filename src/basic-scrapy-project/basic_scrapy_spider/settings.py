# Scrapy settings for quotes_js_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. 

BOT_NAME = 'basic_scrapy_spider'

SPIDER_MODULES = ['basic_scrapy_spider.spiders']
NEWSPIDER_MODULE = 'basic_scrapy_spider.spiders'


#USER_AGENT = 'quotes_js_scraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

SCRAPEOPS_API_KEY = '467d7efe-32c9-45e1-871b-e66f8cc63acc'

SCRAPEOPS_PROXY_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}


# Use the User-agent middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,     # scrapy_fake_useragent
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,      # scrapy_fake_useragent
}