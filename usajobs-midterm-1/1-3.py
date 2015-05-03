import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
total = 0
for country_name in ['China', 'South Africa', 'Tajikistan']:
	atts = {"Country": country_name, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	data = resp.json()
	print("%s has %s job listings." % (country_name, data['TotalJobs']))
	total += int(data['TotalJobs'])

print("Together, they have %s total job listings." % (total))