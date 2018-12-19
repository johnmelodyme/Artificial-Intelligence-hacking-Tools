#/usr/bin/env python
import bs4
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = "https://www.ubuntu.com"
#grabbing command:
uClient = uReq("https://www.ubuntu.com")
page_html = uClient.read()
uClient.close()
page_soup = (page_html, "html.parser")
#grab each ubuntu()
page_soup.findAll = ("div",  {"class" : "Download Ubuntu"}) 
#len(containers)
#containers[0]
container = containers[0]
#for containers in container
download = container.div.div.a["Ubuntu 18.04.1 LTS"]
