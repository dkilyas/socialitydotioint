import sys, requests
from bs4 import BeautifulSoup

def crawl(url):
    sourceCode = requests.get(url)
    if (sourceCode.status_code == 200):
        plainText = sourceCode.text
        crawler = BeautifulSoup(plainText, 'html.parser')
        print(crawler.find_all('head'))



productUrl = str(sys.argv[1])
crawl(productUrl)