import shutil
import requests
url = "http://www.ssa.gov/oact/babynames/names.zip"

resp = requests.get(url)

f = open("/tmp/ssanational.zip", "wb")
f.write(resp.content)
f.close()

shutil.unpack_archive("/tmp/ssanational.zip", "/tmp")

rows2000 = open("/tmp/YOB2000.TXT").readlines()
totes2000 = 0
for r in rows2000:
    if 'Archer' in r:
        totes2000 += int(r.split(',')[2])

rows2010 = open("/tmp/YOB2010.TXT").readlines()
totes2010 = 0
for r in rows2010:
    if 'Archer' in r:
        totes2010 += int(r.split(',')[2])
print((totes2010 - totes2000) / totes2000 * 100)