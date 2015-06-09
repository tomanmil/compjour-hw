import bs4
import requests
response = requests.get('http://www.supremecourt.gov/')
soup = bs4.BeautifulSoup(response.text)
link = soup.select("div.recentdecisions")
print(link)
