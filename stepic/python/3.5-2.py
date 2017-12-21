import csv
import operator

result = {}
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] in result:
            result[row[5]] += 1
        else:
            result[row[5]] = 0

print(max(result, key=lambda key: result[key]))
