# TODO: graph

import json

string = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'

for item in json.loads(string):
    name = item['name']
    parents = item['parents']

    if len(parents):
        print(parents)
