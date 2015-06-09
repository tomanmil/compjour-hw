import csv
from operator import attrgetter
import requests
CSVURL = 'https://data.cityofnewyork.us/api/views/f9bf-2cp4/rows.csv?accessType=DOWNLOAD'
response = requests.get(CSVURL)

data = csv.DictReader(response.text)
rows = list(data)
print(rows[0])
sorted(rows,key=attrgetter('SAT Math Avg. Score'))[0]['SCHOOL NAME']