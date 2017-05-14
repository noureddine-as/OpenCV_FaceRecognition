# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageDatabase.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ManageDatabase(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(446, 337)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.BTN_Add = QtGui.QPushButton(self.centralwidget)
        self.BTN_Add.setGeometry(QtCore.QRect(150, 230, 151, 41))
        self.BTN_Add.setObjectName(_fromUtf8("BTN_Add"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 30, 111, 181))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(160, 30, 251, 181))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.TXT_FisrtName = QtGui.QLineEdit(self.widget1)
        self.TXT_FisrtName.setObjectName(_fromUtf8("TXT_FisrtName"))
        self.verticalLayout_2.addWidget(self.TXT_FisrtName)
        self.TXT_LasttName = QtGui.QLineEdit(self.widget1)
        self.TXT_LasttName.setObjectName(_fromUtf8("TXT_LasttName"))
        self.verticalLayout_2.addWidget(self.TXT_LasttName)
        self.TXT_Branch = QtGui.QLineEdit(self.widget1)
        self.TXT_Branch.setObjectName(_fromUtf8("TXT_Branch"))
        self.verticalLayout_2.addWidget(self.TXT_Branch)
        self.TXT_Level = QtGui.QLineEdit(self.widget1)
        self.TXT_Level.setObjectName(_fromUtf8("TXT_Level"))
        self.verticalLayout_2.addWidget(self.TXT_Level)
        self.TXT_Email = QtGui.QLineEdit(self.widget1)
        self.TXT_Email.setObjectName(_fromUtf8("TXT_Email"))
        self.verticalLayout_2.addWidget(self.TXT_Email)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.BTN_Add.setText(_translate("MainWindow", "Add to Database", None))
        self.label.setText(_translate("MainWindow", "First Name", None))
        self.label_2.setText(_translate("MainWindow", "Last Name", None))
        self.label_3.setText(_translate("MainWindow", "Branch", None))
        self.label_4.setText(_translate("MainWindow", "Level", None))
        self.label_5.setText(_translate("MainWindow", "E-mail", None))
        self.TXT_Branch.setText(_translate("MainWindow", "CSEE - T1", None))
        self.TXT_Level.setText(_translate("MainWindow", "INE2", None))
        self.TXT_Email.setText(_translate("MainWindow", "abcdabcd@gmail.com", None))

