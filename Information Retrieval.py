# Text mining
# 19127558 - Bùi Phú Thịnh
# 19127391 - Tô Vũ Thái Hào

from vncorenlp import VnCoreNLP
import xml.etree.ElementTree as ET
 
# Passing the path of the
# xml document to enable the
# parsing process
tree = ET.parse('24.xml')
 
# getting the parent tag of
# the xml document
root = tree.getroot()
 
# printing the root (parent) tag
# of the xml document, along with
# its memory location
print(root)