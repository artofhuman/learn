import re
import requests

link1 = input()
link2 = input()

link_pattern = r'href="(.*)"'
resp = requests.get(link1)


def find_links(text):
    return re.findall(link_pattern, text)


links = find_links(resp.text)

result = 'No'
for l in links:
    resp = requests.get(l)
    local_links = find_links(resp.text)
    if link2 in local_links:
        result = 'Yes'
        break

print(result)
