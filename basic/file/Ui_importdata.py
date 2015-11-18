# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic/file/Ui_importdata.ui'
#
# Created: Mon Nov 25 08:17:49 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_ImportData(object):
    def setupUi(self, ImportData):
        ImportData.setObjectName(_fromUtf8("ImportData"))
        ImportData.resize(448, 561)
        self.gridLayout_3 = QtGui.QGridLayout(ImportData)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(ImportData)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.textEditImportOutput = QtGui.QPlainTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEditImportOutput.setFont(font)
        self.textEditImportOutput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEditImportOutput.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.textEditImportOutput.setReadOnly(True)
        self.textEditImportOutput.setObjectName(_fromUtf8("textEditImportOutput"))
        self.verticalLayout.addWidget(self.textEditImportOutput)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
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
        self.lineEditIliModelName = QtGui.QLineEdit(self.groupBox)
        self.lineEditIliModelName.setEnabled(False)
        self.lineEditIliModelName.setObjectName(_fromUtf8("lineEditIliModelName"))
        self.gridLayout.addWidget(self.lineEditIliModelName, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditDbSchema = QtGui.QLineEdit(self.groupBox)
        self.lineEditDbSchema.setText(_fromUtf8(""))
        self.lineEditDbSchema.setObjectName(_fromUtf8("lineEditDbSchema"))
        self.gridLayout.addWidget(self.lineEditDbSchema, 2, 1, 1, 1)
        self.cBoxAppModule = QtGui.QComboBox(self.groupBox)
        self.cBoxAppModule.setEnabled(False)
        self.cBoxAppModule.setObjectName(_fromUtf8("cBoxAppModule"))
        self.gridLayout.addWidget(self.cBoxAppModule, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.gridLayout.addWidget(self.dateTimeEdit, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.textEditNotes = QtGui.QPlainTextEdit(self.groupBox)
        self.textEditNotes.setObjectName(_fromUtf8("textEditNotes"))
        self.verticalLayout_2.addWidget(self.textEditNotes)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ImportData)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ImportData)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ImportData.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ImportData.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportData)

    def retranslateUi(self, ImportData):
        ImportData.setWindowTitle(_translate("ImportData", "Import Data", None))
        self.groupBox.setTitle(_translate("ImportData", "Import data ", None))
        self.label_4.setText(_translate("ImportData", "Output:", None))
        self.label.setText(_translate("ImportData", "Input file: ", None))
        self.btnBrowsInputFile.setText(_translate("ImportData", "Browse", None))
        self.lineEditIliModelName.setText(_translate("ImportData", "DM01AVSO24", None))
        self.label_2.setText(_translate("ImportData", "Ili model name: ", None))
        self.label_3.setText(_translate("ImportData", "Project name: ", None))
        self.label_6.setText(_translate("ImportData", "Application module: ", None))
        self.label_5.setText(_translate("ImportData", "Date: ", None))
        self.label_7.setText(_translate("ImportData", "Notes:", None))

