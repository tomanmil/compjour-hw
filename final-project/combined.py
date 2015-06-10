import csv
import json
import string

def cleanaddress(addr):
	exclude = set(string.punctuation)
	return ''.join(ch for ch in addr if ch not in exclude)

f = open('data-hold/establishments_clean.csv', 'r')
g = open('data-hold/restaurant_inspections_clean.csv', 'r')
j = open('data-hold/yelp_academic_dataset_business.json', 'r')
out = open('VegasRestaurants.csv','w')

reader = csv.DictReader(f)
field_names = ['id', 'name', 'address', 'lat', 'lng', 'current_grade', 'current_demerits', 'current_date', 'previous_grade', 'previous_date', 'inspection_history', 'yelp_stars', 'yelp_reviews']
writer = csv.DictWriter(out,fieldnames=field_names)
writer.writeheader()

reader2 = csv.DictReader(g)
insp_records = {}
for insp in reader2:
	record = {}
	record['date'] = insp['inspection_date'].split(' ')[0]
	record['demerits'] = insp['inspection_demerits']
	record['grade'] = insp['inspection_grade']
	record['result'] = insp['inspection_result']
	if insp['permit_number'] in insp_records:
		insp_records[insp['permit_number']].append(record)
	else:
		insp_records[insp['permit_number']] = [record]

yelp_data = []
for data in j: 
	line = json.loads(data)
	if line['state'] == "NV":
		yelp_data.append(line)


print(len(yelp_data))
for row in reader:
	try:
		float(row['lng'])
		d = {}
		d['id'] = row['permit_number']
		d['name'] = row['restaurant_name']
		d['address'] = row['address']
		d['lat'] = row['lat']
		d['lng'] = row['lng']
		d['current_grade'] = row['current_grade']
		d['current_demerits'] = row['current_demerits']
		d['current_date'] = row['date_current'].split(' ')[0]
		d['previous_grade'] = row['previous_grade']
		d['previous_date'] = row['date_previous'].split(' ')[0]
		if row['permit_number'] in insp_records:
			d['inspection_history'] = insp_records[row['permit_number']]
		else:
			d['inspection_history'] = []

		d['yelp_stars'] = 0
		d['yelp_reviews'] = 0

		for yrow in yelp_data:
			addr = yrow['full_address'].split('\n')[0]
			if cleanaddress(addr) == cleanaddress(row['address']):
				d['yelp_stars'] = yrow['stars']
				d['yelp_reviews'] = yrow['review_count']
				break

		writer.writerow(d)
		print("writing %s" % d['id'])
	except:
		pass