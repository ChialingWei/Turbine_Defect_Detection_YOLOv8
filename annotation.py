from lxml import etree
from bs4 import BeautifulSoup
import os

for file in os.listdir('defect_img/ref_annotation/default/'):
    file_name = os.path.join('defect_img/ref_annotation/default/', file)
    xml_parser = etree.XMLParser(encoding='utf-8', recover=True)
    xml_tree = etree.parse(
            file_name,  # This is the path to the file with the XML
            parser=xml_parser
        )
    x = os.path.split(file_name)
    with open(file_name, "r") as file:
        xml_data = file.read()
    soup = BeautifulSoup(xml_data, 'xml')
    h = int(soup.find('nrows').text)
    w = int(soup.find('ncols').text)
    object_elements = soup.find_all('object')
    name = x[1].replace('xml', 'txt')
    with open(f"defect_img/yolo_anno_ref/{name}", 'w') as f:
        for object_elem in object_elements:
            f.writelines('0 ')
            line = []
            pt_elements = object_elem.find_all('pt')
            for pt in pt_elements:
                x = pt.find('x').text
                line.append(str("{:.6f}".format(float(x)/w)))
                line.append(' ')
                y = pt.find('y').text
                line.append(str("{:.6f}".format(float(y)/h)))
                line.append(' ')
            f.writelines(line)
            f.writelines('\n')



