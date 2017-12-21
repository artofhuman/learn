import re
import requests
from urllib.parse import urlparse

result = set()
link_pattern = r'<a.*href=[\'"](.*)'
name_pattern = r'(?!\.{2})(http|ftp|https:\/\/)?((www\.)?[.a-z0-9_-]+\.(?!html)(\w{2,3}))(\/)?.*(\?)?'

link = input()
html = requests.get(link).text

links = re.findall(link_pattern, html)

for link in links:
    m = re.search(name_pattern, link)
    if m:
        result.add(m.group(2))

for i in sorted(result):
    print(i)
