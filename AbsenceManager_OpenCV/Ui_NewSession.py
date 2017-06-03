# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewSession.ui'
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

class Ui_NewSession(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(398, 354)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.BTN_BeginSession = QtGui.QPushButton(self.centralwidget)
        self.BTN_BeginSession.setGeometry(QtCore.QRect(130, 230, 111, 41))
        self.BTN_BeginSession.setObjectName(_fromUtf8("BTN_BeginSession"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 40, 81, 171))
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
        self.widget1.setGeometry(QtCore.QRect(140, 40, 191, 171))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.TXT_Course = QtGui.QLineEdit(self.widget1)
        self.TXT_Course.setObjectName(_fromUtf8("TXT_Course"))
        self.verticalLayout_2.addWidget(self.TXT_Course)
        self.TXT_Date = QtGui.QLineEdit(self.widget1)
        self.TXT_Date.setObjectName(_fromUtf8("TXT_Date"))
        self.verticalLayout_2.addWidget(self.TXT_Date)
        self.TXT_From = QtGui.QLineEdit(self.widget1)
        self.TXT_From.setObjectName(_fromUtf8("TXT_From"))
        self.verticalLayout_2.addWidget(self.TXT_From)
        self.TXT_To = QtGui.QLineEdit(self.widget1)
        self.TXT_To.setObjectName(_fromUtf8("TXT_To"))
        self.verticalLayout_2.addWidget(self.TXT_To)
        self.TXT_Branch = QtGui.QLineEdit(self.widget1)
        self.TXT_Branch.setObjectName(_fromUtf8("TXT_Branch"))
        self.verticalLayout_2.addWidget(self.TXT_Branch)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuQuit = QtGui.QMenu(self.menubar)
        self.menuQuit.setObjectName(_fromUtf8("menuQuit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Absence Manager - New Session", None))
        self.BTN_BeginSession.setText(_translate("MainWindow", "Begin Session", None))
        self.label.setText(_translate("MainWindow", "Course:", None))
        self.label_2.setText(_translate("MainWindow", "Date:", None))
        self.label_3.setText(_translate("MainWindow", "From:", None))
        self.label_4.setText(_translate("MainWindow", "To:", None))
        self.label_5.setText(_translate("MainWindow", "Branch", None))
        self.menuQuit.setWindowTitle(_translate("MainWindow", "Absence Manager - New Session", None))
        self.menuQuit.setTitle(_translate("MainWindow", "Quit", None))

