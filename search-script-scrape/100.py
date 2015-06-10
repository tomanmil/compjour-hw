import requests
import csv
url = "http://transparentcalifornia.com/export/2012-cities.csv"
txt = requests.get(url).text

f = open("/tmp/cities2012.csv", "w")
f.write(txt)
f.close()

f = open("/tmp/cities2012.csv", "r")
rows = list(csv.DictReader(f))
winnercity = rows[1]['Agency']
winnermoney = rows[1]['Total Pay & Benefits']
for r in rows:
	if r['Job Title'] == 'City Manager':
		challenger = r['Total Pay & Benefits']
		if challenger >= winnermoney:
			winnercity = r['Agency']

print(winnercity)
