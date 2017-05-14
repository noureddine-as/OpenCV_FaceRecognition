import xml.etree.ElementTree as et

XML_FILE = "students.xml"

class XmlManager():

    def __init__(self, xml_file = XML_FILE):
        self.xml_file = xml_file
        self.tree = et.parse(self.xml_file)
        self.root = self.tree.getroot()

    def get_LastNames(self):
        names = {}
        i = 0
        while i < len(self.root):
            names.update({i+1 : self.root[i][1].text})
            i += 1
        return names

    def get_FirstNames(self):
        names = {}
        i = 0
        while i < len(self.root):
            names.update({i+1 : self.root[i][0].text})
            i += 1
        return names

    def refresh(self):
        self.xml_file = XML_FILE
        self.tree = et.parse(self.xml_file)
        self.root = self.tree.getroot()

    def addStudent(self, id):     #, firstName, lastName, branch, level, email):
        self.refresh()
        new = et.Element(str(id)) #[id, firstName, lastName, branch, level, email])
        self.root.append(new)
        self.tree.write(self.xml_file)

    def produce_XML(self, dic):
        pass

    def student_block(self, id, firstName, lastName, branch, level, email):
        txt = '\t<student id="' + str(id) + '">\n\t\t<first_name>'
        txt += firstName + '</first_name>\n\t\t<last_name>'
        txt += lastName + '</last_name>\n\t\t<branch>'
        txt += branch + '</branch>\n\t\t<level>'
        txt += level + '</level>\n\t\t<email>'
        txt += email + '</email>\n\t</student>\n\n'
        return txt

    def writeNewXML(self, firstName, lastName, branch, level, email) :
        xml_txt = '<?xml version="1.0" encoding="UTF-8"?>\n<students>\n\n'

        self.refresh()
        txt = open(self.xml_file, "w")
        txt.write(xml_txt)

        for i in range(len(self.root)):
            txt.write(self.student_block(i + 1, self.root[i][0].text, self.root[i][1].text, self.root[i][2].text,
                                    self.root[i][3].text, self.root[i][4].text))

        new_id = len(self.root) + 1
        txt.write(self.student_block(new_id, firstName, lastName, branch, level, email))
        txt.write("</students>")
        txt.close()
        self.refresh()
        return new_id