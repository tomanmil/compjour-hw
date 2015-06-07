import bs4
import requests
response = requests.get('http://www.state.gov/secretary/travel/')
soup = bs4.BeautifulSoup(response.text)
link = soup.select("div#content-output div#content-well div.travel-wrap")
print(link)
