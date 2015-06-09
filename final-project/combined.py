import csv

with open('data-hold/restaurant_establishments.csv','r') as f:
	reader = csv.DictReader(f, delimiter = ';')
	print(reader[0])