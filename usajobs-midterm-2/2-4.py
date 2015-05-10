import json
with open("data-hold/domestic-jobcount.json") as f:
    domestic_data = json.loads(f.read())

domestic_data = sorted(domestic_data)

for d in domestic_data:
	if d[1] < 100:
		print(d[0], ",", d[1])