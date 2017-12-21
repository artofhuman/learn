import xml.etree.ElementTree as ET

string = input()

result = {
    'blue': 0,
    'red': 0,
    'green': 0
}

xml = ET.fromstring(string)


def parse(elem, level):
    color = elem.attrib['color']
    result[color] += level

    childrens = elem.getchildren()
    if len(childrens) == 0:
        return

    for e in childrens:
        parse(e, level + 1)


parse(xml, 1)
print(result['red'], result['green'], result['blue'])
