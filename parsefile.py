'''
https://docs.python.org/2/library/xml.etree.elementtree.html
'''

import xml.etree.ElementTree as ET

def parse_xml_file():
    '''
    xml parse example
    with inline pylint disable for C0103
    '''
    tree = ET.parse('country_dat.xml')
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)

    for neighbor in root.iter('neighbor'):
        print(neighbor.attrib)

    for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get('name')
        print(name, rank)

    for rank in root.iter('rank'):
        new_rank = int(rank.text) + 1
        rank.text = str(new_rank)
        rank.set('updated', 'yes')
    tree.write('output.xml')

    # pylint: disable=C0103
    a = ET.Element('a')
    ET.SubElement(a, 'b')
    c = ET.SubElement(a, 'c')
    ET.SubElement(c, 'd')
    ET.dump(a)
    # pylint: enable=C0103


    tree = ET.parse('actors.xml')
    root = tree.getroot()
    for actor in root.findall('{http://people.example.com}actor'):
        name = actor.find('{http://people.example.com}name')
        print(name.text)
        for char in actor.findall('{http://characters.example.com}character'):
            print(' |-->', char.text)

    # pylint: disable=C0103
    ns = {'real_person': 'http://people.example.com', 'role': 'http://characters.example.com'}

    for actor in root.findall('real_person:actor', ns):
        name = actor.find('real_person:name', ns)
        print(name.text)
        for char in actor.findall('role:character', ns):
            print(' |-->', char.text)
    # pylint: enable=C0103
