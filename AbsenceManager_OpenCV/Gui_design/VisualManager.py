
import sys
from PyQt4 import QtCore, QtGui

from Ui_MainWindow import Ui_MainWindow
from Ui_ManageDatabase import Ui_ManageDatabase
from XmlManager import *
from ImageDbManager import ImageDbManager

class MainWindow_Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BTN_Manage.clicked.connect(self.Manage)
        self.ManagementWindow = None

    def Manage(self):
        self.ManagementWindow = ManageDatabase_Form()
        self.ManagementWindow.show()


class ManageDatabase_Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ManageDatabase()
        self.ui.setupUi(self)
        self.ui.BTN_Add.clicked.connect(self.Add)

    def Add(self):
        xml = XmlManager()
        if (self.ui.TXT_FisrtName.text() != "" and  self.ui.TXT_LasttName.text() != "") :
            new_id = xml.writeNewXML(firstName=self.ui.TXT_FisrtName.text(), lastName=self.ui.TXT_LasttName.text(),
                            branch=self.ui.TXT_Branch.text(), level=self.ui.TXT_Level.text(),
                            email=self.ui.TXT_Email.text())
            db_mgr = ImageDbManager(id=new_id , lastName=str(self.ui.TXT_LasttName.text()))
            db_mgr.run()

        print str(self.ui.TXT_FisrtName.text())
