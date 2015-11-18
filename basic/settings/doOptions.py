# -*- coding: utf-8 -*-

# Import the PyQt and the QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from Ui_options import Ui_Options

class OptionsDialog(QDialog, Ui_Options):
  
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.connect(self.okButton, SIGNAL("accepted()"), self.accept)
        
        # get the settings
        self.settings = QSettings("CatAIS","QGeoApp")
        self.projectsdatabase = self.settings.value("projects/database/path").toString()
        self.projectsdatabasepath = QFileInfo(self.projectsdatabase).absolutePath()
        self.projectsrootpath = self.settings.value("projects/rootdir").toString()
        self.importjarname = self.settings.value("java/import/jarpath").toString()
        self.importjarpath = QFileInfo(self.importjarname).absolutePath()


    def initGui(self):        
        self.lineEditDbPort.setValidator(QRegExpValidator(QRegExp("[0-9]+"), self.lineEditDbPort))        
        
        self.lineEditProjectsDatabase.setText(self.settings.value("projects/database/path").toString()) 
        self.lineEditProjectsRootDir.setText(self.settings.value("projects/rootdir").toString()) 
        
        self.lineEditImportJar.setText(self.settings.value("java/import/jarpath").toString())
        self.plainTextEditImportVMArguments.insertPlainText(self.settings.value("java/import/vmarguments").toString())
        
        self.lineEditDbHost.setText(self.settings.value("db/import/host").toString()) 
        self.lineEditDbDatabase.setText(self.settings.value("db/import/database").toString()) 
        self.lineEditDbPort.setText(self.settings.value("db/import/port").toString()) 
#        self.lineEditDbSchema.setText(self.settings.value("db/import/schema").toString())         
        self.lineEditDbUser.setText(self.settings.value("db/import/user").toString()) 
        self.lineEditDbUserPwd.setText(self.settings.value("db/import/pwd").toString())  
        self.lineEditDbAdmin.setText(self.settings.value("db/import/admin").toString()) 
        self.lineEditDbAdminPwd.setText(self.settings.value("db/import/adminpwd").toString()) 
        
        # set tab order
        QWidget.setTabOrder(self.lineEditDbHost, self.lineEditDbDatabase)
        QWidget.setTabOrder(self.lineEditDbDatabase, self.lineEditDbPort)
        QWidget.setTabOrder(self.lineEditDbPort, self.lineEditDbUser)
        QWidget.setTabOrder(self.lineEditDbUser, self.lineEditDbUserPwd)
        QWidget.setTabOrder(self.lineEditDbUserPwd, self.lineEditDbAdmin)
        QWidget.setTabOrder(self.lineEditDbAdmin, self.lineEditDbAdminPwd)

        self.listWidgetModelRepos.clear()
        size = self.settings.beginReadArray("modelrepositories")
        for i in range(size):
            self.settings.setArrayIndex(i)
            item = QListWidgetItem(self.settings.value("url").toString())
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.listWidgetModelRepos.addItem(item)
        self.settings.endArray();


    @pyqtSignature("on_btnAddModelRepo_clicked()")    
    def on_btnAddModelRepo_clicked(self):
        item = QListWidgetItem("http://")
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        
        self.listWidgetModelRepos.addItem(item)
        self.listWidgetModelRepos.setFocus()
        self.listWidgetModelRepos.setCurrentRow(self.listWidgetModelRepos.count() - 1)


    @pyqtSignature("on_btnDeleteModelRepo_clicked()")    
    def on_btnDeleteModelRepo_clicked(self):
        selectedItems = self.listWidgetModelRepos.selectedItems()
        for selectedItem in self.listWidgetModelRepos.selectedItems():
            self.listWidgetModelRepos.takeItem(self.listWidgetModelRepos.row(selectedItem))


    @pyqtSignature("on_btnBrowseImportJar_clicked()")    
    def on_btnBrowseImportJar_clicked(self):
        file = QFileDialog.getOpenFileName(self, "Open import jar file", self.importjarpath, "JAR (*.jar *.JAR)")
        fileInfo = QFileInfo(file)
        self.lineEditImportJar.setText(QString(fileInfo.absoluteFilePath()))


    @pyqtSignature("on_btnBrowseProjectsDatabase_clicked()")    
    def on_btnBrowseProjectsDatabase_clicked(self):
        file = QFileDialog.getOpenFileName(self, QCoreApplication.translate("QGeoApp", "Choose projects definitions database"), self.projectsdatabasepath,  "DB (*.db *.DB)")
        fileInfo = QFileInfo(file)
        self.lineEditProjectsDatabase.setText(QString(fileInfo.absoluteFilePath()))


    @pyqtSignature("on_btnBrowseProjectsRootDir_clicked()")    
    def on_btnBrowseProjectsRootDir_clicked(self):
        dir = QFileDialog.getExistingDirectory(self, QCoreApplication.translate("QGeoApp", "Choose projects root directory"), self.projectsrootpath)
        dirInfo = QFileInfo(dir)
        self.lineEditProjectsRootDir.setText(QString(dirInfo.absoluteFilePath()))
        

    def accept(self):
        self.settings.setValue("projects/database/path", QVariant(self.lineEditProjectsDatabase.text()))
        self.emit(SIGNAL("projectsFileHasChanged()"))
        
        self.settings.setValue("projects/rootdir", QVariant(self.lineEditProjectsRootDir.text()))
        
        self.settings.setValue("java/import/jarpath", QVariant(self.lineEditImportJar.text()))
        self.settings.setValue("java/import/vmarguments", QVariant(self.plainTextEditImportVMArguments.toPlainText()))

        self.settings.setValue("db/import/host", QVariant(self.lineEditDbHost.text()))   
        self.settings.setValue("db/import/database", QVariant(self.lineEditDbDatabase.text()))      
        self.settings.setValue("db/import/port", QVariant(self.lineEditDbPort.text()))     
        self.settings.setValue("db/import/user", QVariant(self.lineEditDbUser.text())) 
        self.settings.setValue("db/import/pwd", QVariant(self.lineEditDbUserPwd.text())) 
        self.settings.setValue("db/import/admin", QVariant(self.lineEditDbAdmin.text())) 
        self.settings.setValue("db/import/adminpwd", QVariant(self.lineEditDbAdminPwd.text())) 
        
        self.settings.beginWriteArray("modelrepositories");
        for i in range(self.listWidgetModelRepos.count()):
            self.settings.setArrayIndex(i);
            self.settings.setValue("url", self.listWidgetModelRepos.item(i).text());
        self.settings.endArray();        
        
        self.close()
