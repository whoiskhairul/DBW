import requests as req

import csv
import json

data = []

with open('/home/khairul/Downloads/Schulen.csv', 'r', newline='') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        row['www'] = row['WWW'].split(';')
        data.append(row)
with open('/home/khairul/Downloads/testjson.json', 'w') as j:
    json.dump(data, j, indent=4)

print()
r = req.get('http://127.0.0.1:8000/testing/api/schulen/')
print(r.text)


