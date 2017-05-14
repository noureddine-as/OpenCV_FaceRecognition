# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(386, 277)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.BTN_Manage = QtGui.QPushButton(self.centralwidget)
        self.BTN_Manage.setGeometry(QtCore.QRect(80, 40, 231, 51))
        self.BTN_Manage.setObjectName(_fromUtf8("BTN_Manage"))
        self.BTN_OpenSession = QtGui.QPushButton(self.centralwidget)
        self.BTN_OpenSession.setGeometry(QtCore.QRect(80, 130, 231, 51))
        self.BTN_OpenSession.setObjectName(_fromUtf8("BTN_OpenSession"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuQUit = QtGui.QMenu(self.menubar)
        self.menuQUit.setObjectName(_fromUtf8("menuQUit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuQUit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CV Absence Manager", None))
        self.BTN_Manage.setText(_translate("MainWindow", "Manage Database", None))
        self.BTN_OpenSession.setText(_translate("MainWindow", "Open Session", None))
        self.menuQUit.setTitle(_translate("MainWindow", "Quit", None))

