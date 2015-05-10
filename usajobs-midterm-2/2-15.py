import json
import requests
import os
from operator import itemgetter

CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy...")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jobs = json.loads(rawdata)['jobs']

def get_CA_cities(job):
	CA_cities = []
	locs = job['Locations'].split(";")
	for cities in locs:
		if 'California' in cities: 
			CA_cities.append(cities.replace(', California',''))
	return CA_cities

mydict = {}
for job in jobs: 
	cities = get_CA_cities(job)
	for c in cities:
		if c in mydict: 
			mydict[c] += 1
		else:
			mydict[c] = 1

mylist = []
for entry in mydict:
	mylist.append([entry,mydict[entry]])

with open("sample-geochart-cities.html") as f:
    htmlstr = f.read()

sorteddata = sorted(mylist, key = itemgetter(1), reverse = True)

chartdata = [['City', 'Jobs']]
chartdata.extend(sorteddata)

tablerows = []
for d in sorteddata:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

tablerows = "\n".join(tablerows)

with open("2-15.html", "w") as f:
    htmlstr = htmlstr.replace('#CHART_DATA#', str(chartdata))
    htmlstr = htmlstr.replace('#TABLE_ROWS#', tablerows)
    f.write(htmlstr)