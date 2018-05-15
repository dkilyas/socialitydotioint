import sys, requests
from bs4 import BeautifulSoup

def crawl(url):
    sourceCode = requests.get(url)
    if (sourceCode.status_code == 200):
        plainText = sourceCode.text
        crawler = BeautifulSoup(plainText, 'html.parser')
        thePriceBfP = crawler.find_all('span', {'data-bind' : 'markupText:\'currentPriceBeforePoint\''})
        thePriceAfP = crawler.find_all('span', {'data-bind' : 'markupText:\'currentPriceAfterPoint\''})

        if (len(thePriceBfP) == 0 and len(thePriceAfP) == 0):
            print("Sorry, this is not a product page.")
        else:
            print (thePriceBfP[0].string + "," + thePriceAfP[0].string)
    else:
        print("There was a connection problem to the url given.")
    


if (len(sys.argv) > 1):
    productUrl = str(sys.argv[1])
    crawl(productUrl)
else:
    print("You did not provide Url, please just a give the url of the product")