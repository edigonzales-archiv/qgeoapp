# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modules/qnplso/settings/Ui_setdatabase.ui'
#
# Created: Sun Oct 14 17:29:54 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SetDatabase(object):
    def setupUi(self, SetDatabase):
        SetDatabase.setObjectName(_fromUtf8("SetDatabase"))
        SetDatabase.resize(504, 124)
        self.gridLayout_3 = QtGui.QGridLayout(SetDatabase)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(SetDatabase)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEditCadastralSurveyingInputFile = QtGui.QLineEdit(self.groupBox)
        self.lineEditCadastralSurveyingInputFile.setObjectName(_fromUtf8("lineEditCadastralSurveyingInputFile"))
        self.gridLayout.addWidget(self.lineEditCadastralSurveyingInputFile, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(0, 27))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnBrowseCadastralSurveyingInputFile = QtGui.QPushButton(self.groupBox)
        self.btnBrowseCadastralSurveyingInputFile.setObjectName(_fromUtf8("btnBrowseCadastralSurveyingInputFile"))
        self.gridLayout.addWidget(self.btnBrowseCadastralSurveyingInputFile, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SetDatabase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(SetDatabase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SetDatabase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SetDatabase.reject)
        QtCore.QMetaObject.connectSlotsByName(SetDatabase)

    def retranslateUi(self, SetDatabase):
        SetDatabase.setWindowTitle(QtGui.QApplication.translate("SetDatabase", "Additional Database", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SetDatabase", "Set additional database ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SetDatabase", "Cadastral surveying: ", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowseCadastralSurveyingInputFile.setText(QtGui.QApplication.translate("SetDatabase", "Browse", None, QtGui.QApplication.UnicodeUTF8))

