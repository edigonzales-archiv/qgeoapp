# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from Ui_setdatabase import Ui_SetDatabase

class SetDatabaseDialog(QDialog, Ui_SetDatabase):
  
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.connect(self.okButton, SIGNAL("accepted()"), self.accept)
        
        self.settings = QSettings("CatAIS","QGeoApp")
        self.projectId = str(self.settings.value("project/active/id").toString())
        self.cadastralsurveyingspatialitepath = QFileInfo(self.settings.value("qnplso/"+self.projectId+"/cadastralsurveyingspatialitepath").toString()).absolutePath()


    def initGui(self):     
        self.lineEditCadastralSurveyingInputFile.setText(self.settings.value("qnplso/"+self.projectId+"/cadastralsurveyingspatialitepath").toString()) 


    @pyqtSignature("on_btnBrowseCadastralSurveyingInputFile_clicked()")    
    def on_btnBrowseCadastralSurveyingInputFile_clicked(self):
        file = QFileDialog.getOpenFileName(self, QCoreApplication.translate("QGeoApp", "Choose spatialite file"), self.cadastralsurveyingspatialitepath,  "SQLITE (*.sqlite *.SQLITE)")
        fileInfo = QFileInfo(file)
        self.lineEditCadastralSurveyingInputFile.setText(QString(fileInfo.absoluteFilePath()))


    def accept(self):
        self.settings.setValue("qnplso/"+self.projectId+"/cadastralsurveyingspatialitepath", QVariant(self.lineEditCadastralSurveyingInputFile.text()))

        self.close()


