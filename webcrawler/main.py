import sys, requests
from bs4 import BeautifulSoup

def crawl(url):
    sourceCode = requests.get(url)
    if (sourceCode.status_code == 200):
        plainText = sourceCode.text
        crawler = BeautifulSoup(plainText, 'html.parser')
        thePriceBfP = crawler.find_all('span', {'data-bind' : 'markupText:\'currentPriceBeforePoint\''})
        thePriceAfP = crawler.find_all('span', {'data-bind' : 'markupText:\'currentPriceAfterPoint\''})
        print (thePriceBfP[0].string + "," + thePriceAfP[0].string)



productUrl = str(sys.argv[1])
crawl(productUrl)