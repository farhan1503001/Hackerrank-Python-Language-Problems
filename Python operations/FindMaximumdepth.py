import xml.etree.ElementTree as etree

if __name__=='__main__':
    n=int(input().strip())
    xml=''
    for _ in range(n):
        xml+=input()
    
    tree=etree.ElementTree(etree.fromstring(xml))
    