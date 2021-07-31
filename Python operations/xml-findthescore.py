import xml.etree.ElementTree as etree

if __name__=='__main__':
    line=int(input().strip())
    xml=''
    for _ in range(line):
        xml+=input()
    tree=etree.ElementTree(etree.fromstring(xml))
    root=tree.getroot()
    print(sum([len(elem.items()) for elem in tree.iter()]))