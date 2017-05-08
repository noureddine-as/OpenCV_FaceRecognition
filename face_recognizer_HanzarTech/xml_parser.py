import xml.etree.ElementTree as et

xml_file = "students.xml"

def get_LastNames():
    names = {}

    tree = et.parse(xml_file)
    root = tree.getroot()
    i = 0
    while i < len(root):
        names.update({i+1 : root[i][1].text})
        i += 1
    return names

def get_FirstNames():
    names = {}

    tree = et.parse(xml_file)
    root = tree.getroot()
    i = 0
    while i < len(root):
        names.update({i+1 : root[i][0].text})
        i += 1
    return names




print get_LastNames()

