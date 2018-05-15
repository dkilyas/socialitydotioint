import sys, requests
from bs4 import BeautifulSoup

def crawl(url):
    sourceCode = requests.get(url)
    print(sourceCode.status_code)



productUrl = sys.argv[1]
crawl(productUrl)