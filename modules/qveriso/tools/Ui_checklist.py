# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools/Ui_checklist.ui'
#
# Created: Thu Oct  4 14:36:40 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Checklist(object):
    def setupUi(self, Checklist):
        Checklist.setObjectName(_fromUtf8("Checklist"))
        Checklist.setWindowModality(QtCore.Qt.NonModal)
        Checklist.resize(997, 603)
        self.gridLayout = QtGui.QGridLayout(Checklist)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(Checklist)
        self.webView.setProperty("url", QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnClose = QtGui.QPushButton(Checklist)
        self.btnClose.setAutoDefault(False)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.horizontalLayout.addWidget(self.btnClose)
        self.btnPDF = QtGui.QPushButton(Checklist)
        self.btnPDF.setAutoDefault(False)
        self.btnPDF.setObjectName(_fromUtf8("btnPDF"))
        self.horizontalLayout.addWidget(self.btnPDF)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Checklist)
        QtCore.QMetaObject.connectSlotsByName(Checklist)

    def retranslateUi(self, Checklist):
        Checklist.setWindowTitle(QtGui.QApplication.translate("Checklist", "Checkliste", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("Checklist", "Schliessen", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPDF.setText(QtGui.QApplication.translate("Checklist", "PDF", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
