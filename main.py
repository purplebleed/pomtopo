#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import re
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import QApplication, QWidget

def get_without_namespace(element):
	m = re.match('\{.*\}', element.tag)
	return element.tag.replace(m.group(0),"") if m else element.tag

def read_from_path(path):
	for root, subdirs, files in os.walk(path):
		for filename in files:
			if filename[-4:] == ".pom":
				file_path = os.path.join(root,filename)
				tree = ET.parse(file_path)
				root = tree.getroot()
				namespace = get_without_namespace(root)
				for child in root:
					tag = get_without_namespace(child)
					if tag == "groupId":
						print(child.text)
					elif tag == "artifactId":
						print(child.text)
					elif tag == "version":
						print(child.text)
					#print(root.tail)
def main():
	"""app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())"""
	read_from_path('test')

	
if __name__ == '__main__':
	main()
    
