
import sys
from PyQt4 import QtCore, QtGui

from Ui_MainWindow import Ui_MainWindow
from Ui_ManageDatabase import Ui_ManageDatabase
from Ui_NewSession import Ui_NewSession

from ImageDbManager import ImageDbManager

from ProcessingModule import *

import time

class MainWindow_Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BTN_Manage.clicked.connect(self.manage)
        self.ui.BTN_OpenSession.clicked.connect(self.beginNewSession)
        self.ManagementWindow = None
        self.NewSession = None

    def manage(self):
        self.ManagementWindow = ManageDatabase_Form()
        self.ManagementWindow.show()

    def beginNewSession(self):
        self.NewSession = NewSession_Form()
        self.NewSession.show()


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

class NewSession_Form(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_NewSession()
        self.ui.setupUi(self)
        self.ui.BTN_BeginSession.clicked.connect(self.BeginSession)

        self.ui.TXT_Course.setText("Embedded Systems Design")
        self.ui.TXT_Date.setText(time.asctime())
        self.ui.TXT_Branch.setText("Amazing CSEE")

    def BeginSession(self):
        # course, branch, date, d1, d2
        train_recognizer()
        run_recognizer(str(self.ui.TXT_Course.text()), str(self.ui.TXT_Branch.text()),
                       str(self.ui.TXT_Date.text()), str(self.ui.TXT_From.text()), str(self.ui.TXT_To.text()))

