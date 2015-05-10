import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def second(thing):
	return thing[1]

intl_data = sorted(intl_data, key=second, reverse=True)

for d in intl_data:
	if d[1] > 10:
		print(d[0], ",", d[1])