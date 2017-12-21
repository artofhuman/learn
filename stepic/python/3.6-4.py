import requests
import json

client_id = '944894e0e3c713f50c4c'
client_secret = '190dfdb84b06c05c3375d930616bbea7'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)

token = j["token"]
headers = {"X-Xapp-Token": token}

result = {}
url = "https://api.artsy.net/api/artists/{}"
with open('dataset_24476_4.txt') as f:
    for id in f.readlines():
        id = id.strip()
        r = requests.get(url.format(id), headers=headers)
        r.encoding = 'utf-8'
        j = json.loads(r.text)

        result[j['sortable_name']] = int(j['birthday'])

result = sorted(result.items(), key=lambda x: (x[1], x[0]))
print("\n".join([k for k, v in result]))
