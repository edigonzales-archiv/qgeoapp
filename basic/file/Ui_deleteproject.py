# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic/file/Ui_deleteproject.ui'
#
# Created: Wed Oct 31 09:32:37 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DeleteProject(object):
    def setupUi(self, DeleteProject):
        DeleteProject.setObjectName("DeleteProject")
        DeleteProject.resize(381, 116)
        self.gridLayout_3 = QtGui.QGridLayout(DeleteProject)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtGui.QGroupBox(DeleteProject)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cBoxProject = QtGui.QComboBox(self.groupBox)
        self.cBoxProject.setEnabled(True)
        self.cBoxProject.setMinimumSize(QtCore.QSize(0, 0))
        self.cBoxProject.setObjectName("cBoxProject")
        self.gridLayout.addWidget(self.cBoxProject, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setEnabled(True)
        self.label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DeleteProject)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(DeleteProject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DeleteProject.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DeleteProject.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteProject)

    def retranslateUi(self, DeleteProject):
        DeleteProject.setWindowTitle(QtGui.QApplication.translate("DeleteProject", "Delete project", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DeleteProject", "Delete project", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DeleteProject", "Project: ", None, QtGui.QApplication.UnicodeUTF8))

