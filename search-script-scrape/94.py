import csv
from operator import itemgetter
import requests

def cleanscore(score):
	if score == 's':
		return 0
	return int(score)

CSVURL = 'https://data.cityofnewyork.us/api/views/f9bf-2cp4/rows.csv?accessType=DOWNLOAD'
response = requests.get(CSVURL)
f = open("SAT.csv", "w")
f.write(response.text.encode('ascii', 'ignore').decode('ascii'))
f.close()

data = csv.DictReader(open("SAT.csv"))
rows = list(data)
newrows = [[row['SCHOOL NAME'],cleanscore(row['SAT Math Avg. Score'])] for row in rows]
print(sorted(newrows,key=itemgetter(1),reverse=True)[0][0])