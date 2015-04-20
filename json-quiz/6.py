import requests
import json
import os
data_url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
tempfilename = "/tmp/congresslist.json"

if os.path.exists(tempfilename):
    tfile = open(tempfilename, "r")
    j = tfile.read()
else:    
    j = requests.get(data_url).text
    tfile = open(tempfilename, "w")
    tfile.write(j)

tfile.close()
accounts = json.loads(j)

print("A.", len(accounts))

x = 0
for a in accounts:
    if a['followers_count'] > 10000:
        x += 1

print("B.", x)


x = 0
for a in accounts:
    if a['verified']:
        x += 1

print("C.", x)

counts = []
for a in accounts:
    counts.append(a['followers_count'])
maxval = sorted(counts, reverse = True)[0]

print("D.", maxval)


counts = []
for a in accounts:
    counts.append(a['statuses_count'])
maxval = sorted(counts, reverse = True)[0]

print("E.", maxval)


from operator import itemgetter
y = sorted(accounts, key = itemgetter('followers_count'), reverse = True)
x = y[0]

print("F.", x['screen_name'], 'has', x['followers_count'], 'followers')


y = sorted(accounts, key = itemgetter('statuses_count'), reverse = True)
z = sorted(y, key = itemgetter('verified'), reverse = False)
x = z[0]

print("G.", x['screen_name'], 'has', x['statuses_count'], 'tweets')


totes = 0
for a in accounts:
    totes += a['followers_count']

print('H.', round(totes / len(accounts)))


from statistics import median
counts = []
for a in accounts:
    counts.append(a['followers_count'])
med = median(counts)

print('I.', med)
