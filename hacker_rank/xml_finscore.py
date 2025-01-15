import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    return sum(len(n.attrib) for n in node.iter())
    # your code goes here

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))