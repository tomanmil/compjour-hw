from xml.etree.ElementTree import XML
import requests
url = "http://www.justice.gov/feeds/opa/justice-news.xml"
txt = requests.get(url).text

newtxt = txt.split(" ")

total = 0

for n in newtxt:
    if n == '2015-06-05':
        total += 1

print(total)