import csv
import requests
CSVURL = 'https://www.osha.gov/dep/fatcat/fy15_federal-state_summaries.csv'
response = requests.get(CSVURL)

data = csv.DictReader(open("fy15_federal-state_summaries.csv"))
rows = list(data)
len(rows)
print (rows)