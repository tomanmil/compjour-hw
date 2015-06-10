import requests
import csv
url = "https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD"
txt = requests.get(url).text

f = open("/tmp/lottery.csv", "w")
f.write(txt)
f.close()

f = open("/tmp/lottery.csv", "r")
rows = list(csv.DictReader(f))

countthis = []
for r in rows:
    a = r['Winning Numbers']
    countthis.append(a)

from collections import Counter
count = Counter(countthis)
sum = count.most_common()[0]

print(sum)
