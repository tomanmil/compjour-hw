from lxml import html
import requests
response = requests.get('http://travel.state.gov/content/passports/english/alertswarnings.html')
doc = html.fromstring(response.text)
link = doc.cssselect('td.alert ')
print(len(link))
