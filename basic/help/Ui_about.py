# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help/Ui_about.ui'
#
# Created: Wed Sep  5 11:34:32 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(285, 333)
        self.gridlayout = QtGui.QGridLayout(About)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.txtAbout = QtGui.QTextEdit(About)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.txtAbout.setPalette(palette)
        self.txtAbout.setAutoFillBackground(True)
        self.txtAbout.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtAbout.setFrameShadow(QtGui.QFrame.Plain)
        self.txtAbout.setReadOnly(True)
        self.txtAbout.setObjectName(_fromUtf8("txtAbout"))
        self.gridlayout.addWidget(self.txtAbout, 2, 0, 1, 3)
        self.btnHelp = QtGui.QPushButton(About)
        self.btnHelp.setEnabled(False)
        self.btnHelp.setObjectName(_fromUtf8("btnHelp"))
        self.gridlayout.addWidget(self.btnHelp, 3, 0, 1, 1)
        self.btnClose = QtGui.QPushButton(About)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.gridlayout.addWidget(self.btnClose, 3, 2, 1, 1)
        self.btnWeb = QtGui.QPushButton(About)
        self.btnWeb.setObjectName(_fromUtf8("btnWeb"))
        self.gridlayout.addWidget(self.btnWeb, 3, 1, 1, 1)
        self.lblVersion = QtGui.QLabel(About)
        self.lblVersion.setObjectName(_fromUtf8("lblVersion"))
        self.gridlayout.addWidget(self.lblVersion, 1, 0, 1, 2)
        self.lblTitle = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setTextFormat(QtCore.Qt.RichText)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.gridlayout.addWidget(self.lblTitle, 0, 0, 1, 2)

        self.retranslateUi(About)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL(_fromUtf8("clicked()")), About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "QGeoApp About", None, QtGui.QApplication.UnicodeUTF8))
        self.txtAbout.setHtml(QtGui.QApplication.translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHelp.setText(QtGui.QApplication.translate("About", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("About", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.btnWeb.setText(QtGui.QApplication.translate("About", "Web", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVersion.setText(QtGui.QApplication.translate("About", "Version x.x-xxxxxx", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTitle.setText(QtGui.QApplication.translate("About", "QGeoApp", None, QtGui.QApplication.UnicodeUTF8))

