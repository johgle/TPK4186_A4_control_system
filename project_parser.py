
# Table of Contents
# -----------------
# 1. Imported modules
# 2. Parser
# 3. Tester

# 1. Imported modules
# -----------------
import xml.dom.minidom #dom means document

# 2. Parser
# -----------------

class ProjectParser():

    def __init__(self):
        pass

    def parse_project(self, filename):
        document = xml.dom.minidom.parse(filename)
        return document
    

# 3. Tester
# -----------------

parser = ProjectParser()
doc = parser.parse_project("ControlSystemProject.xml")
print(doc)

# https://docs.python.org/3/library/xml.dom.minidom.html