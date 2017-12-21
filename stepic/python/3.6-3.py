import requests

with open('dataset_24476_3.txt') as f:
    numbers = f.read().split("\n")

url = 'http://numbersapi.com/{}/math?json=true'

for n in numbers:
    print(n)
    resp = requests.get(url.format(n)).json()
    if resp['found']:
        print('Interesting')
    else:
        print('Boring')
