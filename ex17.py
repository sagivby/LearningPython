import requests
from bs4 import BeautifulSoup

def getSoupObj(website):
    r = requests.get(website)
    r_html = r.text

    return BeautifulSoup(r.text)

def getAllHeadlineFrom(website):
    headLinesTitles = []
    soup = getSoupObj(website)
    for link in soup.findAll('a'):
        hrefStr = link.string
        try:
            if hrefStr.startswith("\n"):
                headLinesTitles.append(link.string.replace("\n", "").strip())
        except:
            pass
    print "About to print {} headlines:".format(len(headLinesTitles))
    for p in headLinesTitles: print p


websiteLink = "http://www.nytimes.com/"
getAllHeadlineFrom(websiteLink)