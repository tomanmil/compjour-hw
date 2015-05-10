import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def second(thing):
	return thing[1]

intl_data = sorted(intl_data, key=second, reverse=True)

for d in intl_data[0:9]:
	print(d[0], ",", d[1])

others = sum(second(x) for x in intl_data[10:])
print("Others,",others)