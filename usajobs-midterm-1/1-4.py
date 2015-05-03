import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
state_list = ['California', 'Florida', 'New York', 'Maryland']
d = {}
for state_name in state_list:
	atts = {"CountrySubdivision": state_name, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	data = resp.json()
	d[state_name] = int(data['TotalJobs'])

print(d)