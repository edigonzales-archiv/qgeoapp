# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'complexchecks/Ui_createdifferencelayer.ui'
#
# Created: Sun Nov 24 15:45:57 2013
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

class Ui_CreateDifferenceLayer(object):
    def setupUi(self, CreateDifferenceLayer):
        CreateDifferenceLayer.setObjectName(_fromUtf8("CreateDifferenceLayer"))
        CreateDifferenceLayer.resize(346, 457)
        self.gridLayout = QtGui.QGridLayout(CreateDifferenceLayer)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(CreateDifferenceLayer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(CreateDifferenceLayer)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.cmbBoxProjectAfter = QtGui.QComboBox(self.groupBox_2)
        self.cmbBoxProjectAfter.setObjectName(_fromUtf8("cmbBoxProjectAfter"))
        self.gridLayout_5.addWidget(self.cmbBoxProjectAfter, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEditDateAfter = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditDateAfter.setReadOnly(True)
        self.lineEditDateAfter.setObjectName(_fromUtf8("lineEditDateAfter"))
        self.gridLayout_5.addWidget(self.lineEditDateAfter, 1, 1, 1, 1)
        self.textEditAfter = QtGui.QPlainTextEdit(self.groupBox_2)
        self.textEditAfter.setReadOnly(True)
        self.textEditAfter.setObjectName(_fromUtf8("textEditAfter"))
        self.gridLayout_5.addWidget(self.textEditAfter, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(CreateDifferenceLayer)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cmbBoxProjectBefore = QtGui.QComboBox(self.groupBox)
        self.cmbBoxProjectBefore.setObjectName(_fromUtf8("cmbBoxProjectBefore"))
        self.gridLayout_2.addWidget(self.cmbBoxProjectBefore, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditDateBefore = QtGui.QLineEdit(self.groupBox)
        self.lineEditDateBefore.setReadOnly(True)
        self.lineEditDateBefore.setObjectName(_fromUtf8("lineEditDateBefore"))
        self.gridLayout_2.addWidget(self.lineEditDateBefore, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.textEditBefore = QtGui.QPlainTextEdit(self.groupBox)
        self.textEditBefore.setReadOnly(True)
        self.textEditBefore.setObjectName(_fromUtf8("textEditBefore"))
        self.gridLayout_2.addWidget(self.textEditBefore, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(CreateDifferenceLayer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CreateDifferenceLayer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CreateDifferenceLayer.reject)
        QtCore.QMetaObject.connectSlotsByName(CreateDifferenceLayer)

    def retranslateUi(self, CreateDifferenceLayer):
        CreateDifferenceLayer.setWindowTitle(_translate("CreateDifferenceLayer", "Create difference layer", None))
        self.groupBox_2.setTitle(_translate("CreateDifferenceLayer", "After ", None))
        self.label_4.setText(_translate("CreateDifferenceLayer", "Project: ", None))
        self.label_5.setText(_translate("CreateDifferenceLayer", "Date: ", None))
        self.label_6.setText(_translate("CreateDifferenceLayer", "Notes: ", None))
        self.groupBox.setTitle(_translate("CreateDifferenceLayer", "Before ", None))
        self.label_2.setText(_translate("CreateDifferenceLayer", "Date: ", None))
        self.label.setText(_translate("CreateDifferenceLayer", "Project: ", None))
        self.label_3.setText(_translate("CreateDifferenceLayer", "Notes: ", None))

