# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from Ui_setcadastralsurveyingdatabase import Ui_SetCadastralSurveyingDatabase

class SetDatabaseDialog(QDialog, Ui_SetCadastralSurveyingDatabase):
  
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.connect(self.okButton, SIGNAL("accepted()"), self.accept)
        
        self.settings = QSettings("CatAIS","QGeoApp")
        self.spatialitepath = QFileInfo(self.settings.value("qnplso/cadastralsurveyingspatialitepath").toString()).absolutePath()


    def initGui(self):     
        self.lineEditInputFile.setText(self.settings.value("projecqnplso/cadastralsurveyingspatialitepath").toString()) 


    @pyqtSignature("on_btnBrowsInputFile_clicked()")    
    def on_btnBrowsInputFile_clicked(self):
        file = QFileDialog.getOpenFileName(self, QCoreApplication.translate("QGeoApp", "Choose spatialite file"), self.spatialitepath,  "SQLITE (*.sqlite *.SQLITE)")
        fileInfo = QFileInfo(file)
        self.lineEditInputFile.setText(QString(fileInfo.absoluteFilePath()))


    def accept(self):
        self.settings.setValue("qnplso/cadastralsurveyingspatialitepath", QVariant(self.lineEditInputFile.text()))

        self.close()


