# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modules/qnplso/tools/Ui_setcadastralsurveyingdatabase.ui'
#
# Created: Sun Oct 14 17:08:49 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SetCadastralSurveyingDatabase(object):
    def setupUi(self, SetCadastralSurveyingDatabase):
        SetCadastralSurveyingDatabase.setObjectName(_fromUtf8("SetCadastralSurveyingDatabase"))
        SetCadastralSurveyingDatabase.resize(448, 124)
        self.gridLayout_3 = QtGui.QGridLayout(SetCadastralSurveyingDatabase)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(SetCadastralSurveyingDatabase)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEditInputFile = QtGui.QLineEdit(self.groupBox)
        self.lineEditInputFile.setObjectName(_fromUtf8("lineEditInputFile"))
        self.gridLayout.addWidget(self.lineEditInputFile, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(0, 27))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnBrowsInputFile = QtGui.QPushButton(self.groupBox)
        self.btnBrowsInputFile.setObjectName(_fromUtf8("btnBrowsInputFile"))
        self.gridLayout.addWidget(self.btnBrowsInputFile, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SetCadastralSurveyingDatabase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(SetCadastralSurveyingDatabase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SetCadastralSurveyingDatabase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SetCadastralSurveyingDatabase.reject)
        QtCore.QMetaObject.connectSlotsByName(SetCadastralSurveyingDatabase)

    def retranslateUi(self, SetCadastralSurveyingDatabase):
        SetCadastralSurveyingDatabase.setWindowTitle(QtGui.QApplication.translate("SetCadastralSurveyingDatabase", "Cadastrasl Surveying Database", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SetCadastralSurveyingDatabase", "Set cadastral surveying database", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SetCadastralSurveyingDatabase", "Database: ", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowsInputFile.setText(QtGui.QApplication.translate("SetCadastralSurveyingDatabase", "Browse", None, QtGui.QApplication.UnicodeUTF8))

