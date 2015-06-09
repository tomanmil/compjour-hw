import csv
from operator import itemgetter
import requests
CSVURL = 'https://data.cityofnewyork.us/api/views/f9bf-2cp4/rows.csv?accessType=DOWNLOAD'
response = requests.get(CSVURL)
f = open("SAT.csv", "w")
f.write(response.text)
f.close()

data = csv.DictReader(open("SAT.csv"))
rows = list(data)
sorted(rows,key=itemgetter('SAT Math Avg. Score'))[0]['SCHOOL NAME']