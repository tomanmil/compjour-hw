import requests
import json 
response = requests.get('https://analytics.usa.gov/data/live/ie.json')
data = response.json()
print(data['totals']['ie_version']['6.0'])